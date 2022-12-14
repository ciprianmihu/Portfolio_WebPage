from django import forms
from django.forms import TextInput, Textarea, Select
from django.forms.widgets import NumberInput, HiddenInput

from projects.models import ProjectLogo, ProjectFile, ProjectFileComment, ProjectActivityMessage, ProjectPayment


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
                  'project_description', 'other_notes', 'classic_or_modern', 'mature_or_youthful',
                  'feminine_or_masculine', 'playful_or_sophisticated', 'economical_or_luxurious',
                  'geometric_or_organic', 'abstract_or_literal']

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
            'classic_or_modern': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
            'mature_or_youthful': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
            'feminine_or_masculine': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
            'playful_or_sophisticated': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
            'economical_or_luxurious': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
            'geometric_or_organic': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
            'abstract_or_literal': RangeInput(attrs={'max': 100, 'min': -100, 'class': 'form-range'}),
        }


class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['project', 'project_file', 'project_final_file', 'title', 'file_description', 'status']

        widgets = {
            'project': HiddenInput(attrs={'class': 'form-select', 'readonly': 'readonly'}),
            'title': TextInput(attrs={'placeholder': 'Please enter a title', 'class': 'form-control'}),
            'file_description': Textarea(attrs={'placeholder': 'Please enter a description', 'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_file'].widget.attrs['class'] = 'form-control'
        self.fields['project_final_file'].widget.attrs['class'] = 'form-control'


class ProjectFileClientForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['project', 'project_file', 'title', 'file_description', 'status']

        widgets = {
            'project': HiddenInput(attrs={'class': 'form-select', 'readonly': 'readonly'}),
            'title': TextInput(attrs={'placeholder': 'Please enter a title', 'class': 'form-control'}),
            'file_description': Textarea(attrs={'placeholder': 'Please enter a description', 'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_file'].widget.attrs['class'] = 'form-control'


class ProjectFileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['status']

        widgets = {
            'status': Select(attrs={'class': 'form-select'})
        }


class ProjectFileCommentForm(forms.ModelForm):
    class Meta:
        model = ProjectFileComment
        fields = ['project', 'project_file', 'owner', 'comment']

        widgets = {
            'project': HiddenInput(attrs={'class': 'form-select'}),
            'owner': HiddenInput(attrs={'class': 'form-select'}),
            'project_file': HiddenInput(attrs={'class': 'form-select'}),
            'comment': Textarea(attrs={'placeholder': 'Please enter a comment', 'class': 'form-control'}),
        }


class ProjectMessageForm(forms.ModelForm):
    class Meta:
        model = ProjectActivityMessage
        fields = ['project', 'owner', 'title', 'message']

        widgets = {
            'project': HiddenInput(attrs={'class': 'form-select'}),
            'owner': HiddenInput(attrs={'class': 'form-select'}),
            'title': TextInput(attrs={'placeholder': 'Please enter a title', 'class': 'form-control'}),
            'message': Textarea(attrs={'placeholder': 'Please enter a message', 'class': 'form-control'}),
        }


class ProjectPaymentForm(forms.ModelForm):
    class Meta:
        model = ProjectPayment
        fields = ['project', 'owner', 'price']

        widgets = {
            'project': HiddenInput(attrs={'class': 'form-select'}),
            'owner': HiddenInput(attrs={'class': 'form-select'}),
            'price': TextInput(attrs={'placeholder': 'Please enter price', 'class': 'form-control'}),
        }