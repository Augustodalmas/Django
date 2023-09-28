from django.shortcuts import render, redirect
from cars.models import Cars
from cars.forms import CarModelForm
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

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request,'new_car.html',{'new_car_form' : new_car_form})