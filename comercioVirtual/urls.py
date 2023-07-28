"""
URL configuration for comercioVirtual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myAppComercios.views import ProductsList, ProductsDetail, CustomersList, CustomersDetail, SellsList, SellsDetail, UsersAuthenticationList, UsersAuthenticationDetail

from myAppComercios.views import CustomTokenObtainPairView





urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas para el modelo Products
    path('products/', ProductsList.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductsDetail.as_view(), name='products-detail'),

    # Rutas para el modelo Customers
    path('customers/', CustomersList.as_view(), name='customers-list'),
    path('customers/<int:pk>/', CustomersDetail.as_view(), name='customers-detail'),

    # Rutas para el modelo Sells
    path('sells/', SellsList.as_view(), name='sells-list'),
    path('sells/<int:pk>/', SellsDetail.as_view(), name='sells-detail'),

    # Rutas para el modelo Users_Authentication
    path('users/', UsersAuthenticationList.as_view(), name='users-list'),
    path('users/<int:pk>/', UsersAuthenticationDetail.as_view(), name='users-detail'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
