from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

# Leer - Listar todos los productos
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/producto_list.html', {'productos': productos})

# Crear - Añadir un nuevo producto
def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'myapp/producto_form.html', {'form': form})

# Actualizar - Editar un producto existente
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'myapp/producto_form.html', {'form': form})

# Eliminar - Borrar un producto existente
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'myapp/producto_confirm_delete.html', {'producto': producto})
