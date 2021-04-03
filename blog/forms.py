from django import forms
from django.forms import ModelForm
from .models import Blog, BlogCategory

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = BlogForm()


class BlogCategoryForm(ModelForm):
    class Meta:
        model = BlogCategory
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = BlogCategoryForm()
