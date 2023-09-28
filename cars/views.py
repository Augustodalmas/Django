from django.shortcuts import render
from cars.models import Cars
#Esta camada será mostrada ao usuário, como o nome já diz
def cars_views(request):
    cars = Cars.objects.all().order_by('model')
    search = request.GET.get('search') #pega a informação enviada pelo usuário
    if search:
        cars = Cars.objects.filter(model__icontains=search) #Orms do Django

    return render(
        request,
        'cars.html',
        {'cars' : cars} #Informação que está vindo do meu models
        )

#Para não digitar todo o HTML nessa pagina, utilizamos os 'templates' com RENDER