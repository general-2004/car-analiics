from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    model = Car
    fields = "__all__"