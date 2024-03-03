from django.contrib import admin

from .models import Categoria, Receita


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    ...


class ReceitaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
