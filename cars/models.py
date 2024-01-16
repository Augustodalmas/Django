from django.db import models
from django.contrib.auth.models import User
"""
Este arquivo é onde mostramos ao django, um modelo que desejamos criar dentro do banco de dados, tipando seus nomes.
"""


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='car/', blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model


# Criação de um Model para inventario de carros
class CarsInventory(models.Model):
    cars_count = models.IntegerField()
    cars_values = models.FloatField(null=True, )
    # Campo de data com autoincremento da data atual de atualização
    create_at = models.DateTimeField(auto_now_add=True)

    # Classe utilizada pelo django para ordernar a mostra de dados, neste caso, irá mostrar as datas em ordem decrescente por causa do - antes do campo
    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_values}'
