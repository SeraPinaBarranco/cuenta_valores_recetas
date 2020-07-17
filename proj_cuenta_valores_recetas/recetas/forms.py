from django import forms

from .models import Recetas, Productos

class FormRecetas(forms.ModelForm):    
    #nombre_receta= forms.CharField(label='Título', max_length=80)
    def __init__(self, *args, **kwargs):
        super(FormRecetas, self).__init__(*args, **kwargs)    
   
    class Meta:
        model = Recetas
        fields= ['titulo',]

        widgets = {
            'titulo': forms.TextInput(attrs=
                {'class':'form-control ml-3 mb-2 text-center'}),
        }

class FormProductos(forms.ModelForm):    
    #nombre_receta= forms.CharField(label='Título', max_length=80)
    def __init__(self, *args, **kwargs):
        super(FormProductos, self).__init__(*args, **kwargs)    
   
    class Meta:
        model= Productos
        fields= '__all__'

        widgets = {
                'producto': forms.TextInput(attrs=
                    {'class':'form-control ml-3 text-center'}),

                'calorias': forms.TextInput(attrs=
                {'class':'form-control ml-3 text-center'}),

                'grasas': forms.TextInput(attrs=
                    {'class':'form-control ml-3 text-center'}),
            }
        
    
    