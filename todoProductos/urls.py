from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/<int:id>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]
