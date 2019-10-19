from datetime import timedelta
from django.core.signing import TimestampSigner

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db import models


# Create your models here.
class Siteuser(AbstractUser):
    incorrect_attempts = models.PositiveSmallIntegerField(default=0)
    phone_number = models.CharField(max_length=50)
