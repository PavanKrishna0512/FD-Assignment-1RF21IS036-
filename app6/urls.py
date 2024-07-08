from django.contrib import admin
from django.urls import path
from app6 import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface path
    path('register/', views.register, name='register'),  # Path for the customer registration form
    path('products/<cust_id>/', views.products, name='products'),  # Path for the products page, which accepts a customer ID
    path('open_savings_account/<cust_id>/', views.open_savings_account, name='open_savings_account'),  # Path for the savings account form
    path('success/', views.success, name='success'),  # Path for the success page
]
