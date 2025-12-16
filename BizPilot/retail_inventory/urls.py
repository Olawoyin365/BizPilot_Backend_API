from django.urls import path
from .views import (ProductListCreateView, ProductDetailView, CategoryListCreateView)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='product-category'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
