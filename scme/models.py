from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    imagem = models.ImageField(blank=True)
    saldo = models.BigIntegerField()

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=200)
    setor = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Orcamento(models.Model):
    codigo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor_total = models.FloatField(blank=True, null=True)
    quantidade = models.BigIntegerField()
    codigo_vendedor = models.ForeignKey(Vendedor,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)



