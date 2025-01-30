from django.contrib import admin
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
    list_display = ("name", "summary", "content")

admin.site.register(Duet, DuetAdmin)

# material your model here.
class SoporteAdmin(admin.ModelAdmin):
    list_display = ("name","number", "image","tipo_soporte")

admin.site.register(Soporte, SoporteAdmin)