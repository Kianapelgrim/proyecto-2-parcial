from django import forms
from .models import *

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['idEmpleado', 'EmpleadoNombre','EmpleadoEdad','EmpleadoTel','EmpleadoSalario','EmpleadoFechaContratacion','EmpleadoCorreo']
        labels = {'idEmpleado':"codigo de empleado:",
                  'EmpleadoNombre':"Nombre de Empleado:",
                  'EmpleadoEdad':"Edad del empleado:",
                  'EmpleadoTel':"Telefono del empleado:",
                  'EmpleadoSalario':"Salario del empleado:",
                  'EmpleadoCorreo':"Correo del empleado:",
                  'EmpleadoFechaContratacion':"Fecha de contratacion: "}
        widget={'idEmpleado':forms.TextInput,
                'EmpleadoNombre': forms.TextInput,
                'EmpleadoEdad': forms.TextInput,
                'EmpleadoNombre':forms.TextInput,
                'EmpleadoEdad':forms.TextInput,
                'EmpleadoTel':forms.TextInput,
                'EmpleadoSalario':forms.TextInput,
                'EmpleadoCorreo':forms.TextInput,
                'EmpleadoFechaContratacion':forms.TextInput,
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['idProveedor','nombreProveedor','ProveedorDireccion','ProveedorTelefono','ProveedorCorreo']
        labels = {'idProveedor':"codigo de proveedor:",
                  'nombreProveedor':"Nombre de Proveedor:",
                  'ProveedorDireccion':"Direccion del Proveedor:",
                  'ProveedorTelefono':"Telefono del Proveedor:",
                  'ProveedorCorreo':"Correo del Proveedor:",
                 }
        widgets={'idProveedor':forms.TextInput,
                'nombreProveedor': forms.TextInput,
                'ProveedorDireccion':forms.TextInput,
                'ProveedorTelefono':forms.TextInput,
                'ProveedorCorreo':forms.TextInput,
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto','ProductoDescripcion','ProductoPrecio','Inventario','ProductoIngreso']
        labels = {'idProducto':"codigo de producto:",
                  'nombreProducto':"Nombre de producto:",
                  'ProductoDescripcion': "Descripcion del producto:",
                  'ProductoPrecio': "Precio del Producto:",
                  'Inventario':"Cantidad en inventario:",
                  'ProductoIngreso':"Fecha de ingreso del producto:"

                  }
        widget={'idProducto':forms.TextInput,
                'nombreProducto': forms.TextInput,
                'ProductoDescripcion': forms.TextInput,
                'ProductoPrecio': forms.TextInput,
                'Inventario': forms.TextInput,
                'ProductoIngreso':forms.TextInput,
        }

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['idCliente', 'nombreCliente', 'ClienteTelefono','ClienteCorreo','ClienteRegistro']
        labels = {'idCliente':"codigo de Cliente:",
                  'nombreCliente':"Nombre de Cliente:",
                  'ClienteTelefono':"Telefono del Cliente:",
                  'ClienteCorreo':"Correo del Cliente:",
                  'ClienteRegistro':"Fecha de registro del Cliente:"
                  }
        widget={'idCliente':forms.TextInput,
                'nombreCliente': forms.TextInput,
                'ClienteTelefono':forms.TextInput,
                'ClienteCorreo':forms.TextInput,
                'ClienteRegistro':forms.TextInput,
                
        }

class facturaForm(forms.ModelForm):
    class Meta:
        model = Facturas
        fields = ['idFactura','FacturaEmision','idCliente','idProducto','idEmpleado','Subtotal','Total','MetodoPago']
        labels = {'idFactura':"codigo de Factura:",
                  'nombreCliente':"Nombre de Cliente:",
                  'FacturaEmision':"Fecha de emision de Factura:",
                  'idProducto':"Id del Producto:",
                  'idEmpleado': "Id del Empleado:",
                  'Subtotal':"Subtotl:",
                  'Total':"Total:",
                  'MetodoPago':"Metodo de Pago:",
                  }
        widget={'idFactura':forms.TextInput,
                'nombreCliente': forms.TextInput,
                'FacturaEmision': forms.TextInput,
                'idProducto': forms.TextInput,
                'idEmpleado': forms.TextInput,
                'Subtotal': forms.TextInput,
                'Total': forms.TextInput,
                'MetodoPago': forms.TextInput,
        }
        