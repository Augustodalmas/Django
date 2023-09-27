from django.db import models
"""
Este arquivo é onde mostramos ao django, um modelo que desejamos criar dentro do banco de dados, tipando seus nomes.
"""
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Cars(models.Model):
    """
    primary_key = chave primaria, onde tudo se referencia
    Max_length = tamanho máximo de palavras
    Blank = opção de deixar em branco
    Null = opção de deixar nulo
    AutoFiel = auto-incrementar
    CharField = campo de texto
    IntegerField = campo numérico
    FloatFiel = campo de ponto flutuante
    Foreignkey = chave de ligação entre tabelas
    On_delete, serve para dar uma ação quando tentar deletar uma tabela, neste caso, proteger e nao permitir
    Related_name, nome de relação na conexão de tabelas
    ImageField, é um campo de imagens, para botar imagem no produto
    Upload_to, é a referencia para onde vamos dar upload da imagem com django
    """
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='car/', blank=True, null=True)

#Para adicionar ao banco de dados, utilizar "Makimigrations" e após "migrate"
    def __str__(self):
        return self.model
