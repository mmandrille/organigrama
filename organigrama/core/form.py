from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Organismo

class OrganismoForm(ModelForm):
    class Meta:
        model = Organismo
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }