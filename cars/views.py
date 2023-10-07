from cars.models import Cars
from django.http import HttpResponseRedirect
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#Utilizando class listview
class CarsListView(ListView):
    model = Cars
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = Cars.objects.filter(model__icontains=search)
        return cars
    

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