from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin
from applications.home.models import Blog, Material, Duet, Soporte
from django.utils.translation import gettext_lazy as _

# ✅ Filtro personalizado para Parler (porque list_filter no soporta traducciones directamente)
class NameFilter(admin.SimpleListFilter):
    title = _("Nombre")  # Nombre del filtro en el admin
    parameter_name = "name"

    def lookups(self, request, model_admin):
        """ Devuelve una lista de valores disponibles en el filtro. """
        names = set(model_admin.model.objects.values_list("translations__name", flat=True))
        return [(name, name) for name in names if name]

    def queryset(self, request, queryset):
        """ Filtra los resultados en base al valor seleccionado en el filtro. """
        if self.value():
            return queryset.filter(translations__name=self.value())
        return queryset

# ✅ BlogAdmin con soporte para Django-Parler
@admin.register(Blog)
class BlogAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = ("title", "category", "image")
    search_fields = ("translations__title", "translations__category")

# ✅ MaterialAdmin con filtro personalizado
@admin.register(Material)
class MaterialAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = ("name", "tipo", "image")
    search_fields = ("translations__name", "translations__summary")
    list_filter = (NameFilter,)  # ✅ Usamos el filtro personalizado

# ✅ DuetAdmin con filtro personalizado
@admin.register(Duet)
class DuetAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = ("name", "id", "summary", "short_content")
    search_fields = ("translations__name", "translations__summary")
    list_filter = (NameFilter,)  # ✅ Usamos el filtro personalizado

    def short_content(self, obj):
        """ Muestra una versión corta del contenido en el admin """
        return format_html(obj.content[:100] + "...") if obj.content else "No hay contenido"

    short_content.short_description = "Contenido (corto)"

# ✅ SoporteAdmin con soporte para Django-Parler
@admin.register(Soporte)
class SoporteAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = ("name", "number", "image", "tipo_soporte")
    search_fields = ("translations__name", "translations__description")
