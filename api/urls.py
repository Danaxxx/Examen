from django.urls import path
from api.views import apicategoria, apidonacion,apimarca,apipago,apiproducto,apisuscripcion,apiuser,apiProductoDetalle

urlpatterns = [

    path('donacion', apidonacion, name='apiDonacion'),
    path('producto', apiproducto, name='apiProducto'),
    path('categoria', apicategoria, name='apiProducto'),
    path('marca', apimarca, name='apiProducto'),
    path('user', apiuser, name='apiProducto'),
    path('suscripcion', apisuscripcion, name='apiProducto'),
    path('pago', apipago, name='apiProducto'), 
    path('apiProductoDetalle/<buscarId>/', apiProductoDetalle, name='ProductoDetalle'),
]