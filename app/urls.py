"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Esta é a camada onde orientamos nossas URLS do site
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCreateCar, DetailCarsView, UpdateCarsView, DeleteCarView
from accounts.views import register_view, login_view, logout_view
from cars.views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCreateCar.as_view(), name='new_car'),
    path('car/<int:pk>', DetailCarsView.as_view(), name='detail_cars'),
    path('car/<int:pk>/update', UpdateCarsView.as_view(), name='update_car'),
    path('car/<int:pk>/delete', DeleteCarView.as_view(), name='delete_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = handler404