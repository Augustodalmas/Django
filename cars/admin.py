from django.contrib import admin
from cars.models import Cars, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CarAdmin(admin.ModelAdmin):
    #List_display, será os itens que aparecerão no topo de nossa grade
    list_display = ("model", "brand", "factory_year", "model_year", "value")
    #search_fields, são os campos quais podemos filtrar
    search_fields = ("model", "brand")

#Aqui estamos dizendo ao django, que queremos que o modelo Cars, receba a classe CarAdmin como seu filtro de admin.
admin.site.register(Brand, BrandAdmin)
admin.site.register(Cars, CarAdmin)


