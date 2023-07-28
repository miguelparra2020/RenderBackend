from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Models of products.
# Modelo de productos
class Products(models.Model):
    id_product = models.CharField(primary_key=True, max_length=255) #Id of product with key primary, Id del producto con llave primaria
    name = models.TextField(max_length=100) #Name of product, nombre del producto
    description = models.TextField(max_length=300) # Description of product, descripción del producto
    category = models.TextField(max_length=300) # category of product, categoría del producto
    quantity_stock = models.IntegerField() # quantity of stock od product, cantidad en almacenamiento  del producto
    unitary_price = models.IntegerField() #unitary price of product, precio unitario del producto

# Models of customers.
# Modelos de clientes.
class Customers(models.Model):
    id_customer = models.CharField(primary_key=True, max_length=255) # Id of customer with primary key
    # Id del cliente con clave primaria
    name = models.TextField(max_length=100) # Name of customer
    # Nombre del cliente
    telephone = models.IntegerField() # Telephone number of customer
    # Número de teléfono del cliente
    email = models.TextField(max_length=30) # Email address of customer
    # Dirección de correo electrónico del cliente
    city = models.TextField(max_length=50) # City of customer
    # Ciudad del cliente

#Relational Table
#Tabla relacional

# Models of sales.
# Modelos de ventas.
class Sells(models.Model):
    id_sell = models.CharField(primary_key=True, max_length=255) # Id of sale with primary key
    # Id de la venta con clave primaria
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE) # Foreign key to Products
    # Clave foránea hacia Productos
    price_sell = models.IntegerField() # Sale price
    # Precio de venta
    quantity_sell = models.IntegerField() # Sale quantity
    # Cantidad vendida
    id_customer = models.ForeignKey(Customers, on_delete=models.CASCADE) # Foreign key to Customers
    # Clave foránea hacia Clientes

# Models of user authentication.
# Modelos de autenticación de usuarios.
class CustomUserManager(BaseUserManager):
    def create_user(self, user, password, **extra_fields):
        if not user:
            raise ValueError('El nombre de usuario es obligatorio')
        user = self.model(user=user, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True')

        return self.create_user(user, password, **extra_fields)

class Users_Authentication(AbstractBaseUser):
    id_user = models.CharField(primary_key=True, max_length=255)
    user = models.TextField(max_length=100, unique=True)
    name = models.TextField(max_length=100)
    email = models.TextField(max_length=30)
    cellphone = models.IntegerField()
    state = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['name', 'email', 'cellphone']

    def __str__(self):
        return self.user

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser
