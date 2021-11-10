from django import forms
from django.db.models import fields
from .models import WidgetModel

class WidgetForm(forms.ModelForm):
    class Meta:
        model = WidgetModel
        fields = '__all__'

