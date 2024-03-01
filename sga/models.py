from django.db import models

class Licenca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=False, null=False)
    fornecedor = models.CharField(max_length=200, blank=True, null=True)
    licenca = models.CharField(max_length=200, blank=True, null=True)
    quantidade = models.IntegerField(blank=False, null=False)
    data_aquisicao = models.DateField(blank=False, null=False)
    data_expiracao = models.DateField(blank=True, null=True)
    valor_unitario = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.nome