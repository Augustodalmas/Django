from typing import Any
from django.contrib import admin
from cars.models import Cars, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CarAdmin(admin.ModelAdmin):

    list_display = ("model", "brand", "factory_year", "model_year", "value")

    search_fields = ("model", "brand")

    readonly_fields = ("owner",)

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.owner = usuario
        super(CarAdmin, self).save_model(request, obj, form, change)


#Aqui estamos dizendo ao django, que queremos que o modelo Cars, receba a classe CarAdmin como seu filtro de admin.
admin.site.register(Brand, BrandAdmin)
admin.site.register(Cars, CarAdmin)


