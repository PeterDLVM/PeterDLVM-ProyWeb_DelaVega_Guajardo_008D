from django.contrib import admin
from .models import Profile, Producto, BoletaCompra, DetalleCompra

admin.site.register(Producto)

admin.site.register(Profile)

admin.site.register(BoletaCompra)

admin.site.register(DetalleCompra)