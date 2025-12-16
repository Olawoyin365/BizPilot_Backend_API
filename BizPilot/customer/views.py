from rest_framework import generics, permissions
from retail_inventory.models import Product
from .serializers import ProductReadOnlySerializer, OrderSerializer
from .models import Order
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics, permissions
from .serializers import CustomerRegistrationSerializer

# Custom serializer to use email instead of username

class CustomerTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

class CustomerTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomerTokenObtainPairSerializer

# Customer Registration View

class CustomerRegistrationView(generics.CreateAPIView):
    serializer_class = CustomerRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# Product

class ProductListView(generics.ListAPIView):
    """
    Customers browse products filtered by industry
    """
    serializer_class = ProductReadOnlySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()

        # filter by category
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        # Filter by business industry if customer is logged in (restrict to industry-specific inventories)
        customer = getattr(self.request.user, 'customer', None)
        if customer:
            # Only show products whose business owner is in the same industry
            user_industry = self.request.user.customer.industry if hasattr(self.request.user, 'customer') else None
            if user_industry:
                queryset = queryset.filter(created_by__industry=user_industry)

        return queryset

# Customer Order CRUD

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Must be logged in as customer
