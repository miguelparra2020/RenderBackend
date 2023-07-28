from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework import generics
from .models import Products, Customers, Sells, Users_Authentication
from .serializers import ProductsSerializer, CustomersSerializer, SellsSerializer, UsersAuthenticationSerializer

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CustomersList(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class CustomersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class SellsList(generics.ListCreateAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer

class SellsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer

class UsersAuthenticationList(generics.ListCreateAPIView):
    queryset = Users_Authentication.objects.all()
    serializer_class = UsersAuthenticationSerializer

class UsersAuthenticationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users_Authentication.objects.all()
    serializer_class = UsersAuthenticationSerializer


# Resto de importaciones...

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Obtener el nombre de usuario y la contraseña del cuerpo de la solicitud POST
        user = request.data.get("user")
        password = request.data.get("password")

        # Obtener el modelo de usuario personalizado (Users_Authentication)
        User = get_user_model()

        try:
            # Obtener el usuario basado en el nombre de usuario proporcionado
            user_instance = User.objects.get(user=user)  # Accede al administrador a través de la clase User, no de la instancia
        except User.DoesNotExist:
            # Si el usuario no existe, devolver un mensaje de error de autenticación
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña del usuario
        if user_instance.check_password(password):
            # Si la contraseña es válida, generar el token JWT y devolverlo en la respuesta
            refresh = self.get_token(user_instance)
            access_token = str(refresh.access_token)
            return Response({"access_token": access_token})
        else:
            # Si la contraseña no es válida, devolver un mensaje de error de autenticación
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)