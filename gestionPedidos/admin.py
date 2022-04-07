from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class Clientesadmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'telefono')
    search_fields=('nombre', 'telefono')

class Articulosadmin(admin.ModelAdmin):
    list_filter=('seccion',)

class Pedidosadmin(admin.ModelAdmin):
    list_display=('numero', 'fecha')
    list_filter=('fecha',)
    date_hierarchy='fecha'
    

admin.site.register(Clientes, Clientesadmin)
admin.site.register(Articulos, Articulosadmin)
admin.site.register(Pedidos, Pedidosadmin)


