from cars.models import Cars
from django.shortcuts import render
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404


class MainPage(ListView):
    model = Cars
    template_name = '404.html'


# Utilizando class listview
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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DetailCarsView(DetailView):
    model = Cars
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateCarsView(UpdateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('detail_cars', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        car = super().get_object(queryset)

        if car.owner != self.request.user:
            raise Http404("Você não tem permissão para acessar esta página.")
        return car


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteCarView(DeleteView):
    model = Cars
    template_name = 'car_delete.html'
    success_url = '/cars/'


def handler404(request, exception):
    return render(request, '404.html', status=404)
