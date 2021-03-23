from django import forms
from django.forms import ModelForm
from .models import Page

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = PageForm()