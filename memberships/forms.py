from django import forms
from django.forms import ModelForm
from .models import Plan, Member

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = PlanForm()


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = []
        labels = {}
        help_texts = {}
            
form = MemberForm()