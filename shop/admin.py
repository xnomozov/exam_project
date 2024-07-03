from email.headerregistry import Group

from django.contrib import admin
from django.contrib.auth.models import User

from shop.models import Product, Category, Order, Comment


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'image', 'description', 'category', 'discount', 'quantity', 'rating']
    list_display = ('name', 'price', 'image', 'category')
    list_filter = ('category', 'rating', 'created_at',)
    search_fields = ('name', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title',)
    search_fields = ('title',)

    list_filter = ('title',)

    # prepopulated_fields = {'slug': ('title',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')

    class Meta:
        verbose_name = 'comments'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'order_email', 'product')
    list_filter = ('order_name', 'order_email', 'product')
    search_fields = ('order_name', 'order_email', 'product')
    verbose_name = 'orders'
