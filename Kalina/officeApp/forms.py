from django import forms
from .models import OfficeItem


class ItemsForm(forms.ModelForm):
    class Meta:
        model = OfficeItem
        fields = ('__all__')

