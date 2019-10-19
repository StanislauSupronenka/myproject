from django.utils.timezone import now

from users.models import Siteuser
from django.db import models
from enum import Enum


class Status(Enum):
    Denied = 'Denied'
    Access = 'Access'

    @classmethod
    def get_choices(cls):
        return [
            (el.value, name)
            for name, el in cls.__members__.items()
        ]


class Deal(models.Model):
    date = models.DateTimeField(default=now, editable=False)
    owner = models.ForeignKey(
        Siteuser,
        null=True,
        related_name='deals',
        on_delete=models.SET_NULL
    )
    status = models.CharField(
        max_length=6,
        choices=Status.get_choices(),
        default='Saved'
    )
    currency_code = models.CharField(max_length=3)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=4)
    write_off_account = models.CharField(max_length=30)
    income_account = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
