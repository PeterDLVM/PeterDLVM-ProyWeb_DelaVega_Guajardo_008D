from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Index'),
    path('Nuestros-productos/', views.productos_list, name='Nuestros-productos'),
    path('Fundaciones/', views.Fundaciones, name='Fundaciones'),
    path('Mapa/', views.Mapa, name='Mapa'),
    path('Ranking/', views.Ranking, name='Ranking'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('Inicio-sesion-Admin/', views.IniciosesionAdmin, name='Inicio-sesion-Admin'),
    path('Inicio-sesion-Corriente/', views.IniciosesionCorriente, name='Inicio-sesion-Corriente'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),  # URL para el panel de administración de Django
    path('register/', views.register_view, name='register'),
    path('micuenta/', views.micuenta, name='micuenta'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/create/', views.producto_create, name='producto_create'),
    path('producto/<int:pk>/update/', views.producto_update, name='producto_update'),
    path('producto/<int:pk>/delete/', views.producto_delete, name='producto_delete'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:detalle_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    path('mis_boletas/', views.mis_boletas, name='mis_boletas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)