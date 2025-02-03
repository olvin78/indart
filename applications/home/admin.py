from django.contrib import admin
from django.utils.html import format_html  # ✅ Importar format_html correctamente
from applications.home.models import ( Blog,Material,Duet,Soporte)

# Register your models here.

# blog your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "image",)

admin.site.register(Blog,BlogAdmin )

# material your model here.
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "tipo", "image",)

admin.site.register(Material,MaterialAdmin )

# material your model here.
class DuetAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "summary", "short_content")  # ✅ Muestra versión corta del contenido
    search_fields = ("name", "summary")  # ✅ Permite buscar por nombre y resumen
    list_filter = ("name",)  # ✅ Agrega filtros en la barra lateral

    def short_content(self, obj):
        """ Muestra una versión corta del contenido en el admin """
        return format_html(obj.content[:100] + "...") if obj.content else "No hay contenido"

    short_content.short_description = "Contenido (corto)"  # ✅ Nombre visible en el admin

admin.site.register(Duet, DuetAdmin)


# material your model here.
class SoporteAdmin(admin.ModelAdmin):
    list_display = ("name","number","image","tipo_soporte")

admin.site.register(Soporte, SoporteAdmin)