from .models import Income
from django import forms

class Income_Form(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount' , 'income_type' , 'income_note' , 'parent_wallet']