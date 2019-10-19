from django import forms
from django.contrib.auth.hashers import make_password

from users.models import Siteuser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Siteuser
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number"
        )
        widgets = {
            "password": forms.PasswordInput
        }

    def save(self, commit=True):
        password = (
            make_password(
                self.cleaned_data['password']
            )
        )
        self.instance.password = password
        self.cleaned_data['password'] = password
        return super().save(commit)