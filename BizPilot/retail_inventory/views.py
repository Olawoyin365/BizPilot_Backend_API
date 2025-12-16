from rest_framework import generics, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# PRODUCT CATEGORY

class CategoryListCreateView(generics.ListCreateAPIView):
    """
    Business owners can:
    - List product categories
    - Create new product categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

# PRODUCT CRUD

class ProductListCreateView(generics.ListCreateAPIView):
    """
    Business owners can:
    - View all their products
    - Create new products
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return products owned by the logged-in business owner
        return Product.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach product to logged-in business owner
        serializer.save(created_by=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Business owners can:
    - View
    - Update
    - Delete their product
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Prevent access to other users' products
        return Product.objects.filter(created_by=self.request.user)
