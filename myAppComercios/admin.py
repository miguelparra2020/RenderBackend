# Register your models here.
from django.contrib import admin


#importamos el archivo models.py
from .models import Products, Customers, Sells, Users_Authentication


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id_product', 'name', 'description', 'quantity_stock', 'unitary_price']
    search_fields = ['name', 'id_product', 'description']  # Agrega los campos por los que deseas filtrar la búsqueda

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['id_customer', 'name', 'telephone', 'email', 'city']
    search_fields = ['name', 'id_customer', 'email', 'telephone', 'city']

@admin.register(Sells)
class SellsAdmin(admin.ModelAdmin):
    list_display = ['id_sell', 'id_product', 'price_sell', 'quantity_sell', 'id_customer']
    search_fields = ['id_sell', 'id_product', 'id_customer']

@admin.register(Users_Authentication)
class UsersAuthenticationAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'user', 'password', 'name', 'email', 'cellphone', 'state']
    search_fields = ['name', 'id_user', 'user', 'email']