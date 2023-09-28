from django import forms
from cars.models import Brand, Cars

"""
Método bruto
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField()
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Cars(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
"""
    
#método inteligente
class CarModelForm(forms.ModelForm):
    class Meta():
        model = Cars
        fields = '__all__'


#Regras de négocio
    """
        def clean_variavel(self):
        variavel = self.cleaned_data.get('variavel')
        if variavel < 20000:
            self.add_error('Campo_onde_terá_erro', 'Mensagem de erro')
        return variavel
    """
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Preço mínimo de entrada R$20.000')
        return value
    

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O carro deve ser fabricado depois de 1975')
        return factory_year