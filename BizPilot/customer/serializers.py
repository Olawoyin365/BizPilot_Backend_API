from rest_framework import serializers
from .models import Order, OrderItem, Customer
from retail_inventory.models import Product, Category
from django_countries.serializer_fields import CountryField

# Customer Registration

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    country = CountryField(required=False, allow_null=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'country', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        customer = Customer.objects.create(**validated_data)
        return customer

# Products

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductReadOnlySerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'description', 'price', 'quantity', 'category']

# Orders

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'created_at']
        read_only_fields = ['customer', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(customer=self.context['request'].user.customer)
        
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            
            if product.quantity < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for {product.name}. Available: {product.quantity}"
                )
            
            # Deduct stock
            product.quantity -= quantity
            product.save()
            
            # Create OrderItem
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        return order
