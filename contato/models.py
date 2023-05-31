from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class PessoaFisica(Contato):
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class PessoaJuridica(Contato):
    cnpj = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=200)

    def __str__(self):
        return self.razao_social
