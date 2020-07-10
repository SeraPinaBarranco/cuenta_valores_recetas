from django import forms

from .models import Recetas

class FormRecetas(forms.ModelForm):
    
    #nombre_receta= forms.CharField(label='Título', max_length=80)
    
    
    def __init__(self, *args, **kwargs):
        super(FormRecetas, self).__init__(*args, **kwargs)

    
   
    class Meta:
        model = Recetas
        fields= ['titulo',]

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control '}),
        }

    
    