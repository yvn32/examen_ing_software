from urllib.error import ContentTooShortError
from django.shortcuts import render, redirect
from bding.models import ProductoVenta 

def plantilla(request):
    return render(request, "plantilla.html")

def index(request):
    return render(request, "index.html")

def inventario(request):
    productosVenta = ProductoVenta.objects.all()
    contexto = {'inventarioVenta': productosVenta}
    return render(request, "inventario.html", contexto)

def eliminarProductoVenta(request, id):
    productoEliminar = ProductoVenta.objects.get(id=id)
    productoEliminar.delete()
    return redirect('/inventario')

def editarProductoVenta(request, id):
    return redirect('/inventario')

def agregarProductoVenta(request):
    productoAgregar = ProductoVenta.objects.create(
        nombre = "Bicicleta genérica",
        descripcion = "Descripción bicicleta genérica",
        marca = "MasterBikes",
        tipo = "Genérica",
        stock = 3,
        precioCompra = 123456,
        precioVenta = 234567,
        precioVentaProm = 200000,
        idProveedor = 1,
        fecRecepcion = "2022-7-6",
        fecProxCompra = "2023-1-6")

    return redirect('/inventario')
