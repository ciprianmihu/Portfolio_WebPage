from django import forms
from django.forms import TextInput, Textarea

from portfolio.models import PortfolioLogo


class PortfolioLogoForm(forms.ModelForm):
    class Meta:
        model = PortfolioLogo
        fields = ['logo_name', 'logo_description', 'company_name', 'company_description', 'company_industry',
                  'logo_image_1', 'optional_logo_image_2', 'optional_logo_image_3', 'optional_logo_image_4',
                  'optional_logo_image_5', 'optional_logo_image_6']
        widgets = {
            'logo_name': TextInput(attrs={'placeholder': 'Please enter logo name', 'class': 'form-control'}),
            'logo_description': Textarea(
                attrs={'placeholder': 'Please enter logo description', 'class': 'form-control'}),
            'company_name': TextInput(attrs={'placeholder': 'Please enter company name', 'class': 'form-control'}),
            'company_description': Textarea(
                attrs={'placeholder': 'Please enter company description', 'class': 'form-control'}),
            'company_industry': TextInput(
                attrs={'placeholder': 'Please enter company industry', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo_image_1'].widget.attrs['class'] = 'form-control'
        self.fields['optional_logo_image_2'].widget.attrs['class'] = 'form-control'
        self.fields['optional_logo_image_3'].widget.attrs['class'] = 'form-control'
        self.fields['optional_logo_image_4'].widget.attrs['class'] = 'form-control'
        self.fields['optional_logo_image_5'].widget.attrs['class'] = 'form-control'
        self.fields['optional_logo_image_6'].widget.attrs['class'] = 'form-control'
