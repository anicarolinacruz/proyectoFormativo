from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'veterinaria/lista_productos.html', context)


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    context = {'form': form}
    return render(request, 'veterinaria/agregar_producto.html', context)

def eliminar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('lista_productos')

def editar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            if 'imagen' in form.changed_data:
                producto.imagen = form.cleaned_data['imagen']
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    context = {'form': form}
    return render(request, 'veterinaria/editar_producto.html', context)
