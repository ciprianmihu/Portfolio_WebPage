from django import forms
from django.forms import TextInput, Textarea

from services.models import ServiceLogo


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceLogo
        fields = ['service_name', 'service_description', 'service_deliverable', 'turnaround', 'price',
                  'service_image_1']
        widgets = {
            'service_name': TextInput(attrs={'placeholder': 'Please enter service name', 'class': 'form-control'}),
            'service_description': Textarea(
                attrs={'placeholder': 'Please enter service description', 'class': 'form-control'}),
            'service_deliverable': Textarea(
                attrs={'placeholder': 'Please enter deliverables', 'class': 'form-control'}),
            'turnaround': TextInput(attrs={'placeholder': 'Please enter turnaround time', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Please enter service price', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_image_1'].widget.attrs['class'] = 'form-control'
