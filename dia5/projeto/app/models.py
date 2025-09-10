from django.db import models

# Create your models here.
class EnderecoCep(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)

    def __str__(self):
        return f"Rua: {self.rua}, Bairro: {self.bairro}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}"