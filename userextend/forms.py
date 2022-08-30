from datetime import date

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm, UserChangeForm
from django.forms import TextInput, EmailInput, Select, DateInput

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'email_confirmation', 'username', 'gender', 'date_of_birth']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email address', 'class': 'form-control'}),
            'email_confirmation': EmailInput(
                attrs={'placeholder': 'Please confirm your email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter an username', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please confirm your password'

    def clean(self):
        cleaned_data = self.cleaned_data
        users = UserExtend.objects.all()
        for user in users:
            if user.email == cleaned_data.get('email'):
                msg = 'An user with this email already exists!'
                self._errors['username'] = self.error_class([msg])
        today = date.today()
        if cleaned_data.get('date_of_birth') > today:
            msg = 'Birth date cannot be in the future!'
            self.errors['date_of_birth'] = self.error_class([msg])

        return cleaned_data


class UserExtendUpdateForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'email_confirmation', 'username', 'gender', 'date_of_birth']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email address', 'class': 'form-control'}),
            'email_confirmation': EmailInput(
                attrs={'placeholder': 'Please confirm your email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter an username', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserExtendUpdateForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please confirm your password'

    def clean(self):
        cleaned_data = self.cleaned_data
        today = date.today()
        if cleaned_data.get('date_of_birth') > today:
            msg = 'Birth date cannot be in the future!'
            self.errors['date_of_birth'] = self.error_class([msg])

        return cleaned_data


class AuthenticationLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class PasswordChangeFormExtend(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your old password'})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your new password'})


class PasswordResetFormExtend(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email address'})


class SetPasswordFormExtend(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your new password'})
