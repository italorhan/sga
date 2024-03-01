from django.contrib import admin
from sga.models import Licenca, Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LicencaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fornecedor', 'licenca', 'quantidade', 'data_expiracao')
    search_fields = ('nome', 'fornecedor')

admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Licenca, LicencaAdmin)