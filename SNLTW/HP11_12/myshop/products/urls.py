from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),
    path('product/new/', views.product_create, name='product-create'),
    path('product/<int:pk>/edit/', views.product_update, name='product-update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product-delete'),
]
