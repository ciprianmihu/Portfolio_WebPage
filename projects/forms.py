from django import forms
from django.forms import TextInput, Textarea, Select
from django.forms.widgets import NumberInput

from projects.models import ProjectLogo


class RangeInput(NumberInput):
    input_type = 'range'


class ProjectLogoForm(forms.ModelForm):
    class Meta:
        model = ProjectLogo
        fields = ['project_name', 'logo_name', 'logo_slogan', 'company_description', 'company_industry', 'logo_colors',
                  'service_name', 'ready_logo', 'client_name', 'project_description',
                  'optional_project_image_1', 'other_notes', 'status']
        widgets = {
            'project_name': TextInput(attrs={'placeholder': 'Please enter project name', 'class': 'form-control'}),
            'logo_name': TextInput(attrs={'placeholder': 'Please enter logo name', 'class': 'form-control'}),
            'logo_slogan': TextInput(
                attrs={'placeholder': '(Optional) Please enter logo slogan', 'class': 'form-control'}),
            'company_description': Textarea(
                attrs={'placeholder': '(Optional, but helps) Please enter company description',
                       'class': 'form-control'}),
            'company_industry': TextInput(
                attrs={'placeholder': '(Optional) Please enter company industry', 'class': 'form-control'}),
            'logo_colors': TextInput(
                attrs={'placeholder': '(Optional) Please enter logo colors', 'class': 'form-control'}),
            'service_name': Select(attrs={'class': 'form-select'}),
            'ready_logo': Select(attrs={'class': 'form-select'}),
            'client_name': Select(attrs={'class': 'form-select'}),
            'project_description': Textarea(
                attrs={'placeholder': 'Please enter project description', 'class': 'form-control'}),
            'other_notes': Textarea(
                attrs={'placeholder': '(Optional) Please enter other notes', 'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['optional_project_image_1'].widget.attrs['class'] = 'form-control'


class ProjectLogoClientForm(forms.ModelForm):
    class Meta:
        model = ProjectLogo
        fields = ['logo_name', 'logo_slogan', 'company_description', 'company_industry', 'logo_colors',
                  'project_description', 'other_notes', 'style_attribute']
        widgets = {
            'logo_name': TextInput(attrs={'placeholder': 'Please enter logo name', 'class': 'form-control'}),
            'logo_slogan': TextInput(
                attrs={'placeholder': '(Optional) Please enter logo slogan', 'class': 'form-control'}),
            'company_description': Textarea(
                attrs={'placeholder': '(Optional, but helps) Please enter company description',
                       'class': 'form-control'}),
            'company_industry': TextInput(
                attrs={'placeholder': '(Optional) Please enter company industry', 'class': 'form-control'}),
            'logo_colors': TextInput(
                attrs={'placeholder': '(Optional) Please enter logo colors', 'class': 'form-control'}),
            'project_description': Textarea(
                attrs={'placeholder': 'Please enter project description', 'class': 'form-control'}),
            'other_notes': Textarea(
                attrs={'placeholder': '(Optional) Please enter other notes', 'class': 'form-control'}),
            'style_attribute': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-control'}),
        }
