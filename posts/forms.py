from django import forms
from django.forms import ModelForm
from .models import Post, PostCategory, PostOwner

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = PostForm()


class PostCategoryForm(ModelForm):
    class Meta:
        model = PostCategory
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = PostCategoryForm()



class PostOwnerForm(ModelForm):
    class Meta:
        model = PostOwner
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = PostOwnerForm()