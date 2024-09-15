# Create your models here.
# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    country = models.CharField(verbose_name='country', max_length=2, default='NL',
                               null=False, blank=False)
    # status = models.ForeignKey(MembershipStatus, on_delete=models.SET_NULL, null=True, default=1)
