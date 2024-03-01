from django.db import models

class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Licenca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=False, null=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='licenca_fornecedor')
    licenca = models.CharField(max_length=200, blank=True, null=True)
    quantidade = models.IntegerField(blank=False, null=False)
    quantidade_utilizada = models.IntegerField(blank=True, null=True)
    quantidade_disponivel = models.IntegerField(blank=True, null=True)
    data_aquisicao = models.DateField(blank=True, null=True)
    data_expiracao = models.DateField(blank=True, null=True)
    valor_unitario = models.FloatField(blank=False, null=False)
    foto = models.ImageField(upload_to='licenca/', blank=True, null=True)

    def __str__(self):
        return self.nome