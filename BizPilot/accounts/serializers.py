from rest_framework import serializers
from .models import CustomUser
from industries.models import Industry
from django_countries.serializer_fields import CountryField

"""
    Serializer for user signup.
    Converts JSON input into a CustomUser instance.
"""

class UserRegistrationSerializer(serializers.ModelSerializer):
    country = CountryField(required=False, allow_null=True)
    industry = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'country', 'company', 'industry']
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

"""
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', ''),
            country=validated_data.get('country', ''),
            company=validated_data.get('company', ''),
            category=validated_data.get('category', None)
        )
        return user
"""
