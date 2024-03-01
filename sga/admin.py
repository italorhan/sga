from django.contrib import admin
from sga.models import Licenca

class LicencaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fornecedor', 'licenca', 'quantidade', 'data_expiracao')
    search_fields = ('nome', 'fornecedor')

admin.site.register(Licenca, LicencaAdmin)