from django.urls import path
from . import views
from .views import product_form

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('order/<int:client_id>/', views.order_detail, name='order_detail'),
    path('product/add/', product_form, name='product_form'),
]
