BizPilot API Documentation

Project Overview

BizPilot is a modular API platform designed to support multiple industries (Retail, Fashion, Education, etc.). It currently includes:

Accounts app – handles business owner registration, authentication, and management.

Industries app – stores business industry types.

Retail Inventory app – manages products for businesses.

Customers app – handles customer registration, authentication, browsing products, and placing orders.

The API uses Django REST Framework (DRF) with JWT authentication for secure access.

1. Accounts App
Models

CustomUser

Extends Django’s AbstractUser.

Fields:

email (unique)

first_name, last_name

password

phone_number

country

company

industry (ForeignKey to Industries.Industry)

is_staff, is_active

Serializers

UserRegistrationSerializer

Fields: first_name, last_name, email, password, phone_number, country, company, industry.

Handles password hashing during registration.

UserLoginSerializer

Uses JWT via rest_framework_simplejwt.

Login is email-based.

Views

RegisterView

Handles business owner registration.

URL: /api/accounts/signup/

Method: POST

Sample Request Body:

{
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane@example.com",
    "password": "strongpassword",
    "phone_number": "08012345678",
    "country": "Nigeria",
    "company": "MyBiz",
    "industry": 1
}


TokenObtainPairView (JWT)

URL: /api/accounts/token/

Method: POST

Accepts email and password.

TokenRefreshView (JWT)

URL: /api/accounts/token/refresh/

Method: POST

Accepts refresh token.

2. Industries App
Models

Industry

Represents business industries.

Fields:

name (e.g., Retail, Education, Fashion)

Views / Serializers (Optional)

IndustryListView allows fetching all industries for dynamic forms.

URL: /api/industries/

Method: GET

Serializer

IndustrySerializer – returns id and name.

3. Retail Inventory App
Models

Category

Represents product categories within a business.

Fields:

name (e.g., Toiletries, Beverages)

Product

Represents a product in the inventory.

Fields:

name

sku

description

price

quantity

category (ForeignKey to Category)

created_by (ForeignKey to CustomUser)

Serializers

CategorySerializer

Fields: id, name

ProductSerializer

For business owner CRUD.

Fields: id, name, sku, description, price, quantity, category, created_by

Views

Product CRUD Views (Business Owner)

ProductListCreateView: GET all products / POST new product

ProductRetrieveUpdateDestroyView: GET/PUT/DELETE a single product

Category List View

URL: /api/retail_inventory/categories/

GET all product categories.

Endpoints (Business Owner)

/api/retail_inventory/products/ – GET all, POST new

/api/retail_inventory/products/<id>/ – GET, PUT, DELETE single product

/api/retail_inventory/categories/ – GET all categories

4. Customers App
Models

Customer

Fields: first_name, last_name, email, phone_number, country

Order

Fields:

customer (ForeignKey to Customer)

created_at

OrderItem

Fields:

order (ForeignKey to Order)

product (ForeignKey to Product)

quantity

Serializers

CustomerRegistrationSerializer

Fields: first_name, last_name, email, phone_number, country, password

CustomerTokenObtainPairSerializer

JWT login serializer using email as username.

ProductReadOnlySerializer

Fields: id, name, sku, description, price, quantity, category

Category is nested read-only.

OrderSerializer

Handles order creation with multiple OrderItems

Deducts stock automatically

Fields: id, customer, items, created_at

Views

CustomerRegistrationView

URL: /api/customers/signup/

Method: POST

CustomerTokenObtainPairView

URL: /api/customers/token/

Method: POST

Accepts email and password

ProductListView

URL: /api/customers/products/

Method: GET

Optional query param: category=<id>

Optional industry filtering for logged-in customers

OrderCreateView

URL: /api/customers/orders/

Method: POST

Requires JWT authentication

Accepts multiple products in items array

Sample Customer Workflow

Signup

POST /api/customers/signup/


Body:

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "phone_number": "1234567890",
  "country": "Nigeria",
  "password": "strongpassword"
}


Login

POST /api/customers/token/


Body:

{
  "email": "john@example.com",
  "password": "strongpassword"
}


Response: Access & refresh tokens.

Browse Products

GET /api/customers/products/
GET /api/customers/products/?category=2


Place Order

POST /api/customers/orders/
Authorization: Bearer <access_token>


Body:

{
  "items": [
    {"product": 1, "quantity": 2},
    {"product": 3, "quantity": 1}
  ]
}


Stock is deducted automatically

Throws error if requested quantity exceeds available stock

5. Notes

JWT authentication is used for business owners and customers separately.

Industries separate businesses from each other.

Categories are product-specific and independent of industries.

OrderItem allows multiple products per order.

Product browsing can optionally be filtered by category or business industry.

This document serves as a concise reference for all apps, models, serializers, views, and endpoints built from the BizPilot project start to the last customer app features.
