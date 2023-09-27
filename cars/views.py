from django.shortcuts import render
#Esta camada será mostrada ao usuário, como o nome já diz
def cars_views(request):
    return render(request,
                'cars.html',
                {'cars' : {'model' : 'astra 2.0'}} #Informação enviada pelo context ao meu HTML
                )

#Para não digitar todo o HTML nessa pagina, utilizamos os 'templates' com RENDER