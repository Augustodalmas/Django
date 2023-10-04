from cars.models import Cars
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#Esta camada será mostrada ao usuário, como o nome já diz

#Utilizando Função
"""def cars_views(request):
    cars = Cars.objects.all().order_by('model')
    search = request.GET.get('search') #pega a informação enviada pelo usuário
    if search:
        cars = Cars.objects.filter(model__icontains=search) #Orms do Django

    return render(
        request,
        'cars.html',
        {'cars' : cars} #Informação que está vindo do meu models
        )
#Para não digitar todo o HTML nessa pagina, utilizamos os 'templates' com RENDER"""

#Utlizando Class view
"""class CarsView(View):

    def get(self, request):
        cars = Cars.objects.all().order_by('model')
        search = request.GET.get('search') #pega a informação enviada pelo usuário
        if search:
            cars = Cars.objects.filter(model__icontains=search) #Orms do Django

        return render(
            request,
            'cars.html',
            {'cars' : cars} #Informação que está vindo do meu models
            )"""


#Utilizando class listview
class CarsListView(ListView):
    model = Cars #Informa o model
    template_name = 'cars.html' #Informa o template HTML
    context_object_name = 'cars' #Informa o objeto retornado

    #Para realizar um metodo de busca, precisamos criar um metodo de pegar querysets
    def get_queryset(self):
        cars = super().get_queryset().order_by('model') #Ordenar resultados por modelos
        search = self.request.GET.get('search') #Pegar variavel que usuário digita e buscar nos dados
        if search:
            cars = Cars.objects.filter(model__icontains=search) #Se tiver algo escrito, pesquisar pelo mesmo
        return cars
    

#Utilizando Função
"""def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request,'new_car.html',{'new_car_form' : new_car_form})"""

#Utilizando classe view
"""class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(request,'new_car.html',{'new_car_form' : new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILE)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', { 'new_car_form' : new_car_form})"""


#Utilizando classe CreateView
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCreateCar(CreateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class DetailCarsView(DetailView):
    model = Cars
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateCarsView(UpdateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('detail_cars', kwargs={'pk' : self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteCarView(DeleteView):
    model = Cars
    template_name = 'car_delete.html'
    success_url = '/cars/'