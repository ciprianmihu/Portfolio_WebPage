from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject_options = (
        ("i want to hire you", "I want to hire you"),
        ("i want to buy ready made logo", "I want to buy ready made logo"),
        ("i want to ask you", "I want to ask you"))
    subject = forms.ChoiceField(choices=subject_options)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter a message', 'rows': 5}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Please enter your first name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Please enter your last name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Please enter your email'
        self.fields['subject'].widget.attrs['class'] = 'form-control'

