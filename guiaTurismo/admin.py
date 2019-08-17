from django.contrib import admin

from guiaTurismo.models import Ciudades, Categorias, Guias, Tours


class CiudadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion', )


class GuiasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',
                    'frase',
                    'foto',
                    'facebook',
                    'instagram',
                    'telefono',
                    'email',)


class ToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_guia',
                    'nombre',
                    'precio',
                    'url_imagen_mapa',
                    'id_categoria')


admin.site.register(Ciudades, CiudadesAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Guias, GuiasAdmin)
admin.site.register(Tours, ToursAdmin)