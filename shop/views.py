from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from shop.forms import CommentForm, OrderForm, ProductForm, LoginForm, RegisterForm
from shop.models import Product, Category, Comment, CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request, slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if slug:
        products = products.filter(category__slug=slug)

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)
    filter_expensive = request.GET.get('expensive')
    filter_cheap = request.GET.get('cheap')
    if filter_expensive:
        products = products.order_by('-price')[:3]
    elif filter_cheap:
        products = products.order_by('price')[:3]
    context = {'products': products,
               'categories': categories,
               'search_query': search_query,
               }
    return render(request, 'shop/home.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    comments = Comment.objects.filter(product__slug=slug)[0:3]
    comment_form = CommentForm()
    order_form = OrderForm()
    new_comment = None  # Comment posted
    new_order = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        order_form = OrderForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()

        elif order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.product = product
            new_order.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Product successfully ordered'
            )
    return render(request, 'shop/detail.html', {'product': product,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form,
                                                'new_order': new_order,
                                                'order_form': order_form,
                                                'related_products': related_products, })


def about(request):
    return render(request, 'shop/about.html')



def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('home')

    return render(request, 'shop/add-product.html', {'form': form})



def delete_product(request, slug):
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect('home')


def edit_product(request, slug):
    product = Product.objects.get(slug=slug)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'shop/update-product.html', context)


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'form': form}
    return render(request, 'shop/auth/login.html', context)


def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'shop/auth/logout.html', )


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            user.is_active = True
            user.is_staff = True
            user.save()
            login(request, user)
            return redirect('home')
    context = {'form': form}

    return render(request, 'shop/auth/register.html', context )
