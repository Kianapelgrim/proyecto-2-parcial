from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Empleados(models.Model):
    idEmpleado = models.IntegerField(primary_key=True)
    EmpleadoNombre = models.CharField(max_length=50)
    EmpleadoEdad= models.SmallIntegerField()
    EmpleadoTel = models.CharField(validators=[RegexValidator(r'^\d+$', message='Only numbers are allowed.')],max_length=8)
    EmpleadoSalario= models.IntegerField()
    EmpleadoFechaContratacion= models.DateField()
    EmpleadoCorreo= models.EmailField()
    def __str__(self) :
        return str(self.idEmpleado)+ " "  + self.EmpleadoNombre + " "+ str(self.EmpleadoEdad)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    idProovedor = models.ForeignKey(Empleados,null=False, blank=False, on_delete=models.PROTECT  )
    ProductoDescripcion= models.CharField(max_length=100)
    ProductoPrecio= models.IntegerField()
    Inventario= models.IntegerField()
    ProductoIngreso= models.DateField()

    def __str__(self):
        return str(self.idProducto) + " " + self.nombreProducto
    
class Proveedores(models.Model):
    idProveedor=models.IntegerField(primary_key=True)
    nombreProveedor= models.CharField(max_length=50)
    ProveedorDireccion= models.CharField(max_length=100)
    ProveedorTelefono= models.CharField(validators=[RegexValidator(r'^\d+$', message='Only numbers are allowed.')],max_length=8)
    ProveedorCorreo= models.EmailField()

    def __str__(self):
        return str(self.idProveedor) + " " + self.nombreProveedor
    
class Cliente(models.Model):
     idCliente=models.IntegerField(primary_key=True)
     nombreCliente= models.CharField(max_length=50)
     ClienteTelefono= models.CharField(validators=[RegexValidator(r'^\d+$', message='Only numbers are allowed.')],max_length=8)
     ClienteCorreo= models.EmailField()
     ClienteRegistro= models.DateField()

     def __str__(self):
        return str(self.idCliente) + " " + self.nombreCliente
    
class Facturas(models.Model):
    idFactura= models.IntegerField(primary_key=True)
    FacturaEmision= models.DateField()
    nombreCliente=models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.PROTECT)
    idProducto=models.ForeignKey(Producto,null=False, blank=False, on_delete=models.PROTECT)
    idEmpleado=models.ForeignKey(Empleados,null=False, blank=False, on_delete=models.PROTECT)
    Subtotal= models.IntegerField()
    Total= models.IntegerField()
    MetodoPago= models.CharField(max_length=20)
    
    

