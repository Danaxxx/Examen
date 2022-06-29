from django.db import models
# al crear un modelo se debe ejecutar los comandos 
# makemigrations y migrate
# Create your models here.
class Marca(models.Model):
    nombreMarca = models.TextField(max_length=100)
    activoMarca = models.BooleanField()

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    nombreCategoria = models.TextField(max_length=100)
    activoCategoria = models.BooleanField()
    

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=90)
    precioProducto = models.IntegerField()
    precioCosto = models.IntegerField()
    stockProducto = models.IntegerField()
    descripcionProducto = models.TextField(max_length=600)
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marcaProducto = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.nombreProducto

class Usuario(models.Model):
    run = models.TextField(max_length=10)
    dv = models.TextField(max_length=1)    
    nombreUsuario = models.TextField(max_length=20)
    email = models.TextField(max_length=30)
    password = models.TextField()
    tipoDeUsuario = models.TextField()

    def __str__(self):
        return self.run

class tipoUsuario(models.Model):
    nombreTipoUsuario = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreTipoUsuario

class Suscripcion(models.Model):
    runSus = models.TextField(max_length=10)
    dvSus = models.TextField(max_length=1)    
    nombreSus = models.TextField(max_length=20)
    apellidoSus = models.TextField(max_length=20)
    emailSus = models.TextField(max_length=30)
    celularSus = models.TextField(max_length=11)
    tipoDeUsuario = models.TextField()   
    activoSus = models.BooleanField()
    def __str__(self):
        return self.runSus

class medioPago(models.Model):
    nombreMedio =  models.TextField()
    activoMedio = models.BooleanField()

    def __str__(self):
        return self.nombreMedio

class Donacion(models.Model):
    nombreDonante = models.TextField()
    apellidoDonante = models.TextField()
    montoDonacion = models.TextField()
    medioDePago = models.TextField() 
    def __str__(self):
        return self.nombreDonante
