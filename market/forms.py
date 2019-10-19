from django import forms
from django.contrib.auth.hashers import make_password

from users.models import Siteuser
from market.models import Deal


class CreateDealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = (
            "write_off_account",
            "currency_code",
            "currency_rate",
            "income_account",
            "amount"
        )

    def save(self, commit=True):
        return super().save(commit)