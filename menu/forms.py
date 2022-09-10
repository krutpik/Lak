from django import forms

from .models import Description


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}