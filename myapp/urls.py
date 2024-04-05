from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('order/<int:client_id>/', views.order_detail, name='order_detail'),
]
