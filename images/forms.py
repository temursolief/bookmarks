from django import forms
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'slug', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }