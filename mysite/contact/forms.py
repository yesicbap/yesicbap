from django.core import validators
from django import forms
from contact.models import Contact_us



class Contact_usForm(forms.ModelForm):
    """Form definition for Contact_us."""

    class Meta:
        """Meta definition for Contact_usform."""

        model = Contact_us
        fields = ('first_name','last_name','email','message')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'your last name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your email here'}),
            'message': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'your message to us', 'aria-label':'With textarea'}),
        }



