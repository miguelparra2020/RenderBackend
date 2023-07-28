from rest_framework import serializers
from .models import Products, Customers, Sells, Users_Authentication

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class SellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sells
        fields = '__all__'

class UsersAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_Authentication
        fields = '__all__'
