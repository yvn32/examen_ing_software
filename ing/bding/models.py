from django.db import models

# Create your models here.
class ProductoVenta(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    stock = models.IntegerField()
    precioCompra = models.IntegerField()
    precioVenta = models.IntegerField()
    precioVentaProm = models.IntegerField()
    idProveedor = models.IntegerField()
    fecRecepcion = models.DateField()
    fecProxCompra = models.DateField()

