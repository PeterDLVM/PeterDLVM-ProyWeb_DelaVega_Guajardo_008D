from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Profile, Producto, DetalleCompra, BoletaCompra
from .forms import ProductoForm
from django.db import transaction
from django.db.models import Sum


def index(request):
    return render(request, 'Index.html')

def Nuestrosproductos(request):
    return render(request, 'Nuestros-productos.html')

def Fundaciones(request):
    return render(request, 'Fundaciones.html')

def Mapa(request):
    return render(request, 'Mapa.html')

def Ranking(request):
    return render(request, 'Ranking.html')

def conocenos(request):
    return render(request, 'Index.html#conocenos')

def IniciosesionAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('Index')
            else:
                return redirect('Inicio-sesion-Admin')
    return render(request, 'Inicio-sesion-Admin.html')

def IniciosesionCorriente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'Inicio-sesion-Corriente.html')

def logout_view(request):
    logout(request)
    return redirect('Index')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.profile.fecha_nacimiento = fecha_nacimiento
            user.save()
            messages.success(request, '¡Muchas gracias por registrarte!')
            return redirect('Index')

    return render(request, 'index.html')

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'profile': profile})

@login_required
def micuenta(request):
    profile = request.user.profile

    if request.method == 'POST':
        profile.primer_nombre = request.POST.get('primer_nombre')
        profile.segundo_nombre = request.POST.get('segundo_nombre')
        profile.apellido_paterno = request.POST.get('apellido_paterno')
        profile.apellido_materno = request.POST.get('apellido_materno')
        profile.direccion = request.POST.get('direccion')
        profile.celular = request.POST.get('celular')
        profile.save()

        return redirect('micuenta')

    return render(request, 'micuenta.html', {'profile': profile})


def productos_list(request):
    productos = Producto.objects.all()
    return render(request, 'Nuestros-productos.html', {'productos': productos})

@login_required
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_form.html', {'producto': producto})

@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('Nuestros-productos')  # Redirige a la página de listado de productos
        else:
            # En caso de que el formulario no sea válido, muestra los errores al usuario
            messages.error(request, 'Corrija los errores a continuación.')
    else:
        form = ProductoForm()
    
    return render(request, 'producto_form.html', {'form': form})

@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('Nuestros-productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form})

@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('Nuestros-productos')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    try:
        boletacompra = BoletaCompra.objects.get(usuario=request.user, estado_pedido='recibido')
    except BoletaCompra.DoesNotExist:
        boletacompra = BoletaCompra.objects.create(usuario=request.user, estado_pedido='recibido')

    detalle, created = DetalleCompra.objects.get_or_create(
        producto=producto,
        boletacompra=boletacompra,
        defaults={'cantidad': 1, 'subtotal': producto.precio}
    )

    if not created:
        detalle.cantidad += 1
        detalle.subtotal = detalle.cantidad * producto.precio
        detalle.save()

    # Actualizar el contador del carrito en la sesión
    if 'carrito_total' in request.session:
        request.session['carrito_total'] += 1
    else:
        request.session['carrito_total'] = 1

    messages.success(request, f'{producto.nombre} agregado al carrito.')
    return redirect('Nuestros-productos')

@login_required
def carrito(request):
    try:
        boletacompra = BoletaCompra.objects.filter(usuario=request.user, estado_pedido='recibido').first()
        if not boletacompra:
            raise BoletaCompra.DoesNotExist
        detalles_compra = boletacompra.detalles.all()
        total_carrito = sum(detalle.subtotal for detalle in detalles_compra)
    except BoletaCompra.DoesNotExist:
        detalles_compra = []
        total_carrito = 0

    context = {
        'detalles_compra': detalles_compra,
        'total_carrito': total_carrito,
    }
    return render(request, 'carrito.html', context)

@login_required
def eliminar_del_carrito(request, detalle_id):
    detalle_compra = get_object_or_404(DetalleCompra, pk=detalle_id)
    detalle_compra.delete()

    # Restar uno al contador del carrito en la sesión del usuario
    if 'carrito_total' in request.session and request.session['carrito_total'] > 0:
        request.session['carrito_total'] -= 1

    messages.success(request, 'Producto eliminado del carrito exitosamente.')
    return redirect('carrito')
    
@login_required
def confirmar_compra(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                boletacompra = BoletaCompra.objects.select_for_update().filter(usuario=request.user, estado_pedido='recibido').first()
                if not boletacompra:
                    raise BoletaCompra.DoesNotExist
                
                detalles_compra = boletacompra.detalles.all()
                total_boleta = sum(detalle.subtotal for detalle in detalles_compra)

                # Cambiar el estado de la boleta a 'confirmado' u otro estado apropiado
                boletacompra.estado_pedido = 'confirmado'
                boletacompra.save()

                # Limpiar el carrito de compras después de confirmar la compra
                boletacompra.detalles.all().delete()

                # Aquí deberías mostrar los detalles de compra y confirmar la compra
                context = {
                    'boleta': boletacompra,
                    'detalles_compra': detalles_compra,
                    'total_boleta': total_boleta,
                }
                request.session['carrito_total'] = 0
                return render(request, 'resumen_compra.html', context)
        
        except BoletaCompra.DoesNotExist:
            messages.error(request, 'No se encontró una boleta de compra válida.')
            return redirect('carrito')
        except Exception as e:
            messages.error(request, f'Error al confirmar la compra: {str(e)}')
            return redirect('carrito')

    else:
        # Si el método no es POST, redirige a la página correspondiente
        return redirect('carrito')
@login_required
def mis_boletas(request):
    boletas = BoletaCompra.objects.filter(usuario=request.user).order_by('-fecha_compra')

    for boleta in boletas:
        detalles = boleta.detalles.all()
        total_boleta = detalles.aggregate(total=Sum('subtotal'))['total']
        boleta.total_boleta = total_boleta

    return render(request, 'mis_boletas.html', {'boletas': boletas})