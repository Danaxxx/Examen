from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class productoform(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProducto', 'precioProducto','precioCosto', 'stockProducto', 'descripcionProducto', 'categoriaProducto', 'marcaProducto', 'imagen']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1' , 'password2']

class CustomUseradmForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1' , 'password2','is_superuser','is_staff']