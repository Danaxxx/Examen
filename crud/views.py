from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoform
from crud.models import Marca, Categoria, Producto, Usuario, tipoUsuario, Suscripcion, medioPago, Donacion
from django.contrib.auth.decorators import login_required , permission_required
from .forms import  CustomUserForm, CustomUseradmForm
from django.contrib.auth import  authenticate, login
# Create your views here.



def contactView(request):
    return render(request, 'contact.html', {})

def EmpForgotView(request):
    return render(request, 'EmpForgot.html', {})

def EmpFormularioView(request):
    return render(request, 'EmpFormulario.html', {})

def EmpIndexView(request):
    return render(request, 'EmpIndex.html', {})

def EmpResetView(request):
    return render(request, 'EmpReset.html', {})



def macInd1View(request):
    return render(request, 'macInd1.html', {})

def macInd2View(request):
    return render(request, 'macInd2.html', {})

def macInd3View(request):
    return render(request, 'macInd3.html', {})


def indexView(request):
    return render(request, 'index.html', {})

def marcaView(request):
    return render(request, 'marca.html', {'marca': 'constanza'})
 
def paginaenprocesoView(request):
    return render(request, 'paginaenproceso.html', {})
 


#MARCA ----------------------------------------------------------------------------------------------------
def marcaLeerView(request, id):
    contexto = {}
    try:
        fila = Marca.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories
    return render(request, 'marca.html', contexto)

def marcaView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreMarca = request.POST["txtNombre"]
        activoMarca = False
        if 'chkActivo' in request.POST:
            activoMarca = True
        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(nombreMarca) < 5:
                contexto = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    Marca.objects.create(nombreMarca = nombreMarca, activoMarca = activoMarca) 
                else:
                    fila = Marca.objects.get(pk = id)
                    fila.nombreMarca = nombreMarca
                    fila.activoMarca = activoMarca
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        
        elif 'btnListar' in request.POST:
            listado = Marca.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Marca.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories        
    return render(request, 'marca.html', contexto)



#PRODUCTO  ----------------------------------------------------------------------------------------------------
def nuevo_productoView(request): 
    data = {
        'form' : productoform()
    }
    if request.method == 'POST':
        formulario = productoform(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
    return render (request, 'nuevo_producto.html' , data )


def tiendaView(request): 
    data = {
        'productos' : Producto.objects.all()
    }
    return render (request, 'tienda.html', data)



def productoLeerView(request, id):
    contexto = {}
    try:
        fila = Producto.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    contexto["productCategories"] = productCategories
    contexto["productBrand"] = productBrand

    return render(request, 'producto.html', contexto)

def productoView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreProducto = request.POST["txtNombre"]
        precioProducto = request.POST["txtPrecioProducto"]
        precioCosto = request.POST["txtPrecioCosto"]
        stockProducto = request.POST["txtStockProducto"]
        descripcionProducto = request.POST["txtDescripcion"]
        categoriaProducto = request.POST["ctProducto"]
        marcaProducto = request.POST["ctMarca"]
        

        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(nombreProducto) < 5:
                contexto = {'error': 'El nombre del producto debe tener como minimo 5 caracteres'}
            elif len(precioProducto) < 3:
                contexto = {'error': 'El  precio producto debe tener como minimo 3 caracteres'}
            elif len(precioCosto) < 3:
                contexto = {'error': 'El  precio costo debe tener como minimo 3 caracteres'}
            elif len(stockProducto) < 1:
                contexto = {'error': 'El stock producto debe tener como minimo 1 caracteres'}
            elif (categoriaProducto) == '0':
                contexto = {'error': 'Debe seleccionar la marca del producto'}
            elif (marcaProducto) == '0':
                contexto = {'error': 'Debe seleccionar la marca del producto'}

        
            elif id < 1: # ORM Object relational Mapping
                Producto.objects.create(nombreProducto = nombreProducto, precioProducto = precioProducto, precioCosto = precioCosto, stockProducto = stockProducto, descripcionProducto = descripcionProducto, categoriaProducto = categoriaProducto, marcaProducto = marcaProducto)
                contexto = {'mensaje': 'Los datos fueron guardados'}  
            else:
                fila = Producto.objects.get(pk = id)
                fila.nombreProducto = nombreProducto
                fila.precioProducto = precioProducto
                fila.precioCosto = precioCosto
                fila.stockProducto = stockProducto
                fila.descripcionProducto = descripcionProducto
                fila.categoriaProducto = categoriaProducto
                fila.marcaProducto = marcaProducto
                fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Producto.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Producto.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    contexto["productCategories"] = productCategories
    contexto["productBrand"] = productBrand

    return render(request, 'producto.html', contexto)


#CATEGORIA  ----------------------------------------------------------------------------------------------------
def categoriaLeerView(request, id):
    contexto = {}
    try:
        fila = Categoria.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories
    return render(request, 'categoria.html', contexto)

def categoriaView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreCategoria = request.POST["txtNombre"]
        activoCategoria = False
        if 'chkActivo' in request.POST:
            activoCategoria = True

        # detectar que botón fue presionado

        if 'btnGrabar' in request.POST:
            if len(nombreCategoria) < 5:
                contexto = {'error': 'El nombre de la marca debe tener como minimo 5 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    Categoria.objects.create(nombreCategoria = nombreCategoria, activoCategoria = activoCategoria) 
                else:
                    fila = Categoria.objects.get(pk = id)
                    fila.nombreCategoria = nombreCategoria
                    fila.activoCategoria = activoCategoria
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Categoria.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Categoria.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories        
    return render(request, 'categoria.html', contexto)

#USUARIO  ----------------------------------------------------------------------------------------------------

def registro_administrador(request): 
    data = {
        'form':CustomUseradmForm()
    } 
    if request.method == 'POST':
        formulario = CustomUseradmForm(data=request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to= 'registroadm')
        data ["form"] = formulario
    return render (request, 'registration/registroadm.html' , data  )

def registro_usuario(request): 
    data = {
        'form':CustomUserForm()
    } 
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to= 'index')
        data ["form"] = formulario
    return render (request, 'registration/registroadm.html' , data )



def usuarioLeerView(request, id):
    contexto = {}
    try:
        fila = Usuario.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    userCategories = tipoUsuario.objects.all()
    contexto["userCategories"] = userCategories   

    return render(request, 'usuario.html', contexto)

def usuarioView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        run = request.POST["txtRun"]
        dv = request.POST["txtDv"]
        nombreUsuario = request.POST["txtNombreUsuario"]
        email = request.POST["txtEmail"]
        password = request.POST["txtPassword"]
        tipoDeUsuario = request.POST["ctTipoDeUsuario"]
   

        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(run) < 7:
                contexto = {'error': 'El run debe tener como minimo 7 caracteres'}
            elif len(dv) < 1:
                contexto = {'error': 'El  digito verificador debe tener como minimo 1 caracteres'}
            elif len(nombreUsuario) < 3:
                contexto = {'error': 'El  nombre de usuario debe tener como minimo 3 caracteres'}
            elif len(email) < 5:
                contexto = {'error': 'El email  debe tener como minimo 1 caracteres'}
            elif len(password) < 5:
                contexto = {'error': 'La contraseña debe tener mínimo 5 caracteres'}
            elif (tipoDeUsuario) == '0':
                contexto = {'error': 'Debe seleccionar tipoDeUsuario del Usuario'}

        
            elif id < 1: # ORM Object relational Mapping
                Usuario.objects.create(run = run, dv = dv, nombreUsuario = nombreUsuario, email = email, password = password, tipoDeUsuario = tipoDeUsuario)
                contexto = {'mensaje': 'Los datos fueron guardados'}  
            else:
                fila = Usuario.objects.get(pk = id)
                fila.run = run
                fila.dv = dv
                fila.nombreUsuario = nombreUsuario
                fila.email = email
                fila.password = password
                fila.tipoDeUsuario = tipoDeUsuario
                fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Usuario.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Usuario.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}
    userCategories = tipoUsuario.objects.all()
    contexto["userCategories"] = userCategories   

    return render(request, 'usuario.html', contexto)

#PRODUCTO 2 (ADMINISTRADOR)  ----------------------------------------------------------------------------------------------------
def usuarioAdmLeerView(request, id):
    contexto = {}
    try:
        fila = Usuario.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}

    return render(request, 'usuarioAdm.html', contexto)

def usuarioAdmView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        run = request.POST["txtRun"]
        dv = request.POST["txtDv"]
        nombreUsuario = request.POST["txtNombreUsuario"]
        email = request.POST["txtEmail"]
        password = request.POST["txtPassword"]
        tipoDeUsuario = request.POST["ctTipoDeUsuario"]

        

        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:       
            if id < 1: # ORM Object relational Mapping
                Usuario.objects.create(run = run, dv = dv, nombreUsuario = nombreUsuario, email = email, password = password, tipoDeUsuario = tipoDeUsuario)
                contexto = {'mensaje': 'Los datos fueron guardados'}  
            else:
                fila = Usuario.objects.get(pk = id)
                fila.run = run
                fila.dv = dv
                fila.nombreUsuario = nombreUsuario
                fila.email = email
                fila.password = password
                fila.tipoDeUsuario = tipoDeUsuario
                fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Usuario.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Usuario.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    return render(request, 'usuarioAdm.html', contexto)


#TIPO USUARIO  ----------------------------------------------------------------------------------------------------
def tipoUsuarioLeerView(request, id):
    contexto = {}
    try:
        fila = tipoUsuario.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    userCategories = tipoUsuario.objects.all()
    contexto["userCategories"] = userCategories
    return render(request, 'tipoUsuario.html', contexto)

def tipoUsuarioView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreTipoUsuario = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(nombreTipoUsuario) < 5:
                contexto = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    tipoUsuario.objects.create(nombreTipoUsuario = nombreTipoUsuario, activo = activo) 
                else:
                    fila = tipoUsuario.objects.get(pk = id)
                    fila.nombreTipoUsuario = nombreTipoUsuario
                    fila.activo = activo
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        
        elif 'btnListar' in request.POST:
            listado = tipoUsuario.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = tipoUsuario.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}
    userCategories = tipoUsuario.objects.all()
    contexto["userCategories"] = userCategories       
    return render(request, 'tipoUsuario.html', contexto)

#SUSCRIPCION ----------------------------------------------------------------------------------------------------
def suscripcionView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        runSus = request.POST["txtRun"]
        dvSus = request.POST["txtDv"]
        nombreSus = request.POST["txtNombre"]
        apellidoSus = request.POST["txtApellido"]
        emailSus = request.POST["txtEmail"]
        celularSus = request.POST["txtCelular"]
        activoSus = False        
        if 'chkActivo' in request.POST:
            activoSus = True
      

        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(runSus) < 7:
                contexto = {'error': 'El run debe tener como minimo 7 caracteres'}
            elif id < 1: # ORM Object relational Mapping
                Suscripcion.objects.create(runSus = runSus, dvSus = dvSus, nombreSus = nombreSus, apellidoSus = apellidoSus, emailSus = emailSus, celularSus = celularSus, tipoDeUsuario = 2, activoSus = activoSus)
                contexto = {'mensaje': 'Los datos fueron guardados'}  
            else:
                fila = Suscripcion.objects.get(pk = id)
                fila.runSus = runSus
                fila.dvSus = dvSus
                fila.nombreSus = nombreSus
                fila.apellidoSus = apellidoSus
                fila.emailSus = emailSus
                fila.celularSus = celularSus
                fila.tipoDeUsuario = 2
                fila.activoSus = activoSus
                fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Suscripcion.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Suscripcion.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}
  

    return render(request, 'suscripcion.html', contexto)

#SUSCRIPCION ADMINISTRATIVO  ----------------------------------------------------------------------------------------------------
def suscripcionAdmLeerView(request, id):
    contexto = {}
    try:
        fila = Suscripcion.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}

    return render(request, 'suscripcionAdm.html', contexto)

def suscripcionAdmView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        runSus = request.POST["txtRun"]
        dvSus = request.POST["txtDv"]
        nombreSus = request.POST["txtNombre"]
        apellidoSus = request.POST["txtApellido"]
        emailSus = request.POST["txtEmail"]
        celularSus = request.POST["txtCelular"]
 
        activoSus = False        
        if 'chkActivo' in request.POST:
            activoSus = True
      

        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(runSus) < 7:
                contexto = {'error': 'El run debe tener como minimo 7 caracteres'}
            elif id < 1: # ORM Object relational Mapping
                Suscripcion.objects.create(runSus = runSus, dvSus = dvSus, nombreSus = nombreSus, apellidoSus = apellidoSus, emailSus = emailSus, celularSus = celularSus, tipoDeUsuario = 2, activoSus = activoSus)
                contexto = {'mensaje': 'Los datos fueron guardados'}  
            else:
                fila = Suscripcion.objects.get(pk = id)
                fila.runSus = runSus
                fila.dvSus = dvSus
                fila.nombreSus = nombreSus
                fila.apellidoSus = apellidoSus
                fila.emailSus = emailSus
                fila.celularSus = celularSus
                fila.tipoDeUsuario = 2
                fila.activoSus = activoSus
                fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Suscripcion.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Suscripcion.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    return render(request, 'suscripcionAdm.html', contexto)

#MEDIO PAGO  ----------------------------------------------------------------------------------------------------
def medioPagoLeerView(request, id):
    contexto = {}
    try:
        fila = medioPago.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    payCategories = medioPago.objects.all()
    contexto["payCategories"] = payCategories
    return render(request, 'medioPago.html', contexto)

def medioPagoView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreMedio = request.POST["txtNombre"]
        activoMedio = False
        if 'chkActivo' in request.POST:
            activoMedio = True

        # detectar que botón fue presionado

        if 'btnGrabar' in request.POST:
            if len(nombreMedio) < 5:
                contexto = {'error': 'El nombre del medio de pago debe tener como minimo 5 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    medioPago.objects.create(nombreMedio = nombreMedio, activoMedio = activoMedio) 
                else:
                    fila = medioPago.objects.get(pk = id)
                    fila.nombreMedio = nombreMedio
                    fila.activoMedio = activoMedio
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = medioPago.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = medioPago.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    payCategories = medioPago.objects.all()
    contexto["payCategories"] = payCategories        
    return render(request, 'medioPago.html', contexto)


#DONACION ----------------------------------------------------------------------------------------------------
def donacionLeerView(request, id):
    contexto = {}
    try:
        fila = medioPago.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    payCategories = medioPago.objects.all()
    contexto["payCategories"] = payCategories
    return render(request, 'donacion.html', contexto)

def donacionView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreDonante = request.POST["txtNombre"]
        apellidoDonante = request.POST["txtApellido"]
        montoDonacion = request.POST["txtMonto"]
        medioDePago = request.POST["ctMedioPago"]


        # detectar que botón fue presionado

        if 'btnGrabar' in request.POST:
            if len(nombreDonante) < 1:
                contexto = {'error': 'El nombre debe tener como minimo 1 caracter'}
            elif len(montoDonacion) < 2:
                contexto = {'error': 'La donacion tener como minimo 2 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    Donacion.objects.create(nombreDonante= nombreDonante, apellidoDonante = apellidoDonante, montoDonacion = montoDonacion, medioDePago = medioDePago) 
                else:
                    fila = Donacion.objects.get(pk = id)
                    fila.nombreDonante = nombreDonante
                    fila.apellidoDonante = apellidoDonante
                    fila.montoDonacion = montoDonacion
                    fila.medioDePago = medioDePago
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Donacion.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Donacion.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    payCategories = medioPago.objects.all()
    contexto["payCategories"] = payCategories        
    return render(request, 'donacion.html', contexto)

#SUSCRIPCION ADMINISTRATIVO  ----------------------------------------------------------------------------------------------------
def donacionAdmLeerView(request, id):
    contexto = {}
    try:
        fila = Donacion.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}

    return render(request, 'donacionAdm.html', contexto)

def donacionAdmView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreDonante = request.POST["txtNombre"]
        apellidoDonante = request.POST["txtApellido"]
        montoDonacion = request.POST["txtMonto"]
        medioDePago = request.POST["ctMedioPago"]
 

        # detectar que botón fue presionado
        if 'btnListar' in request.POST:
            listado = Donacion.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Donacion.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    return render(request, 'donacionAdm.html', contexto)