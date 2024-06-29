from django.contrib import admin
from django.urls import path
from shop.views import home, details

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', details, name='product_detail'),
]
