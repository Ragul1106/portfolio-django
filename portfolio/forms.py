from django import forms
from .models import Project, ContactMessage
from django.core.validators import validate_email

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email(email)
        return email