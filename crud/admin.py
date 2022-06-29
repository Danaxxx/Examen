from django.contrib import admin
from .models import Marca, Categoria, Producto, Usuario, tipoUsuario, Suscripcion, medioPago, Donacion
# Register your models here.

    #class MarcaAdmin(admin.ModelAdmin):
    #list_display=["nombre","activo"] 
   # list_editable = ["activo"]
   # search_fields= ["activo"]
 


admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(tipoUsuario)
admin.site.register(Suscripcion)
admin.site.register(medioPago)
admin.site.register(Donacion)


