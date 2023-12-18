# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EnquiryForm(forms.Form):
    name_add = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    contact = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "autocomplete": "off",
                "type": "number"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "rows": 2
            }
        ))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "rows": 2
            }
        ))
    note = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "rows": 2
            }
        ))
    date = forms.DateTimeField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control date",
                "type": "date"
            }
        ))
    follow_up_date = forms.DateTimeField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control date",
                "type": "date"
            }
        ))
    assigned = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    reference = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            "placeholder": "",
            "class": "form-control"
        }),
        choices=[
            ("", "Select"),
            ("1", "Ref #001"),
        ])

    source = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            "placeholder": "",
            "class": "form-control"
        }),
        choices=[
            ("", "Select"),
            ("1", "Word Of Mouth"),
        ])
    current_class = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            "placeholder": "",
            "class": "form-control"
        }),
        choices=[
            ("", "Select"),
            ("1", "Class 1"),
        ])
    no_of_child = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))


class VisitorForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
