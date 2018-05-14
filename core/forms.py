from django import forms

from .models import LayerData


class LayerDataform(forms.ModelForm):

    class Meta:
        model = LayerData
        fields = ('layer_name', 'file')