from django.db import models

class Pessoa(models.Model):
    TIPO_CHOICES = (
        ('fisica', 'Pessoa Física'),
        ('juridica', 'Pessoa Jurídica'),
    )
    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    razao_social = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
