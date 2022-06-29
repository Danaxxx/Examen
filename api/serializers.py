import marshal
from rest_framework import serializers
from crud.models import Donacion, Producto, Marca, Categoria, Suscripcion,medioPago
from django.contrib.auth.models import User


class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = ['nombreDonante', 'apellidoDonante', 'montoDonacion', 'medioDePago']


class medioSerializer(serializers.ModelSerializer):
    class Meta:
        model = medioPago
        fields = ['nombreMedio' , 'activoMedio']

class productoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Producto
        fields = ['nombreProducto' , 'precioProducto', 'stockProducto','descripcionProducto','categoriaProducto','marcaProducto', 'imagen']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombreCategoria' ]

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombreMarca' ]


class SuscripcionSerializer(serializers.ModelSerializer):
     class Meta:
        model = Suscripcion
        fields = ['runSus' , 'dvSus', 'nombreSus','apellidoSus','emailSus','celularSus', 'tipoDeUsuario', 'activoSus']

class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name','email','is_staff','is_superuser', 'date_joined', 'password']