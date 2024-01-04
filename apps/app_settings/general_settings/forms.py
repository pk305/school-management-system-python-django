from django import forms
from .models import SchSettings


class GenSettingForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    class Meta:
        model = SchSettings
        fields = ['name', 'email']
