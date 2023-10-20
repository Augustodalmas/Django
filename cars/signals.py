from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Cars, CarsInventory

# Para não haver repetição de código, foi centralizado uma função onde essa função
# Pega o valor total de carros cadastrados, pega o valor da soma de todos os carros, e envia para o model CarsInventory
# Assim criando um inventario de carros com registro de data e hora de modificação


def car_inventory_update():
    cars_count = Cars.objects.all().count()
    cars_values = Cars.objects.aggregate(
        total_values=Sum('value')
    )['total_values']
    CarsInventory.objects.create(
        cars_count=cars_count,
        cars_values=cars_values
    )


@receiver(pre_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Bio gerada automatica"
        # Podemos usar OpenAI para gerar bio de carros automatica, utilizando modelo, marca e ano, porém é uma funcionalidade paga!


@receiver(post_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    # O "SAVE" serve tanto para criação de instancia quanto para atualização, podemos separar da seguinte forma
    """
    def car_pre_save(sender, instance, created **kwargs):
        if created:
            car_inventory_update()
    """
    # Assim será separado o método de create do metodo de Update!
    car_inventory_update()


@receiver(post_delete, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    car_inventory_update()


"""
#O decorator serve para dizer que estamos recebendo a informação de alguem, onde informamos a tabela pelo 'sender'
@receiver(metodo_a_ser_executado, sender=tabela_que_sera_alterada)
def nome_qualquer(sender, instance, **kwargs):
    #sender = tabela que envia o evento
    #instance = informações que estão sendo enviados, podemos retornar todos os valores de models pela instance
    lógica
"""
