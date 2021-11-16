from django import forms
from currency.models import Registrator


class RegForms(forms.ModelForm):
    class Meta:
        model = Registrator
        fields = (
            "login",
            "passwords",
            "mails",
        )
