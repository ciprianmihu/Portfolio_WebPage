from django import forms
from django.forms import TextInput, Textarea, Select

from projects.models import ProjectLogo


class ProjectLogoForm(forms.ModelForm):
    class Meta:
        model = ProjectLogo
        fields = ['project_name', 'logo_name', 'logo_slogan', 'company_description', 'company_industry', 'logo_colors',
                  'service_name', 'ready_logo', 'client_name', 'project_description',
                  'optional_project_image_1', 'other_notes']
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
                attrs={'placeholder': '(Optional) Please enter other notes', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['optional_project_image_1'].widget.attrs['class'] = 'form-control'

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     projects_logo = ProjectLogo.objects.all()
    #     for project_logo in projects_logo:
    #         if project_logo.project_name == cleaned_data.get('project_name'):
    #             msg = 'This projects already exists'
    #             self.errors['project_name'] = self.error_class([msg])
    #     return cleaned_data


class ProjectLogoClientForm(forms.ModelForm):
    class Meta:
        model = ProjectLogo
        fields = ['project_name', 'logo_name', 'logo_slogan', 'company_description', 'company_industry', 'logo_colors',
                  'service_name', 'ready_logo', 'project_description',
                  'optional_project_image_1', 'other_notes']
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
            'project_description': Textarea(
                attrs={'placeholder': 'Please enter project description', 'class': 'form-control'}),
            'other_notes': Textarea(
                attrs={'placeholder': '(Optional) Please enter other notes', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['optional_project_image_1'].widget.attrs['class'] = 'form-control'