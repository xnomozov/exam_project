from django.contrib import admin
from django.urls import path
from shop.views import home, product_detail, about, add_product, delete_product, edit_product, login_page, logout_page, \
    register, add_comment, add_order

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>', product_detail, name='product_detail'),
    path('category/<slug:slug>/products', home, name='category_products'),
    path('about', about, name='about'),
    path('add-product', add_product, name='add_product'),
    path('delete/<slug:slug>', delete_product, name='delete_product'),
    path('product/<slug:slug>/edit', edit_product, name='edit_product'),
    path('login', login_page, name='login'),
    path('logout', logout_page, name='logout'),
    path('register', register, name='register'),
    path('add-comment/<slug:slug>', add_comment, name='add_comment'),
    path('add-order/<slug:slug>', add_order, name='add_order'),

]
