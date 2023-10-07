from django import forms
from cars.models import Brand, Cars

class CarModelForm(forms.ModelForm):
    class Meta():
        model = Cars
        fields = '__all__'



    def __init__(self, *args, **kwargs):
        super(CarModelForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget = forms.TextInput(attrs={'readonly': 'readonly'})



    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Preço mínimo de entrada R$10.000')
        return value
    

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O carro deve ser fabricado depois de 1975')
        return factory_year