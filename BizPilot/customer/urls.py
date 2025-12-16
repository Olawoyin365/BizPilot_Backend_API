from django.urls import path
from .views import ProductListView, OrderCreateView,  CustomerRegistrationView, CustomerTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='customer-product-list'), # Browse Products
    path('orders/', OrderCreateView.as_view(), name='customer-create-order'), # Create Orders
    path('signup/', CustomerRegistrationView.as_view(), name='customer-signup'), 
    path('login/', CustomerTokenObtainPairView.as_view(), name='customer-token-obtain'), # JWT Login
    path('token/refresh/', TokenRefreshView.as_view(), name='customer-token-refresh'),
]
