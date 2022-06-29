from django.urls import path
from . import views
urlpatterns = [
        path('marca', views.marcaView, name="marca"),
        path('marca/<int:id>/', views.marcaLeerView, name="marca"),
        path('categoria', views.categoriaView, name="categoria"),
        path('categoria/<int:id>/', views.categoriaLeerView, name="categoria"),
        path('index', views.indexView, name="index"),
       
        path('registroadm/', views.registro_administrador, name="registroadm"),
        path('EmpForgot', views.EmpForgotView, name="EmpForgot"),
        path('EmpFormulario', views.EmpFormularioView, name="EmpFormulario"),
        path('registrar/', views.registro_usuario, name="registrar"),
        path('EmpReset', views.EmpResetView, name="EmpReset"),
      
        path('macInd1', views.macInd1View, name="macInd1"),
        path('macInd2', views.macInd2View, name="macInd2"),
        path('macInd3', views.macInd3View, name="macInd3"),
      
       
        path('producto/<int:id>/', views.productoLeerView, name="producto"),
        path('producto', views.productoView, name="producto"),
        path('usuario', views.usuarioView, name="usuario"),
        path('usuarioAdm', views.usuarioAdmView, name="usuarioAdm"),
        path('usuarioAdm/<int:id>/', views.usuarioAdmLeerView, name="usuarioAdm"),
        path('tipoUsuario/<int:id>/', views.tipoUsuarioLeerView, name="tipoUsuario"),
        path('tipoUsuario', views.tipoUsuarioView, name="tipoUsuario"),
        path('suscripcion', views.suscripcionView, name="suscripcion"),
        path('suscripcionAdm', views.suscripcionAdmView, name="suscripcionAdm"),
        path('suscripcionAdm/<int:id>/', views.suscripcionAdmLeerView, name="suscripcionAdm"),
        path('medioPago/<int:id>/', views.medioPagoLeerView, name="medioPago"),
        path('medioPago', views.medioPagoView, name="medioPago"),
        path('donacion/<int:id>/', views.donacionLeerView, name="donacion"),
        path('donacion', views.donacionView, name="donacion"),
        path('donacionAdm', views.donacionAdmView, name="donacionAdm"),
        path('donacionAdm/<int:id>/', views.donacionAdmLeerView, name="donacionAdm"),       
        path('paginaenproceso', views.paginaenprocesoView, name="paginaenproceso"), 
        path('tienda/', views.tiendaView,  name='tienda' ) ,
        path('nuevo-producto/', views.nuevo_productoView,  name='nuevo_producto' )      
            ]