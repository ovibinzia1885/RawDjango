from django import forms
from .models import permission
class permission1(forms.ModelForm):
    class Meta:
        model=permission
        fields=('title','name','pdf')