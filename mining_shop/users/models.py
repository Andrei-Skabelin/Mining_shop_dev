from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):

    email = models.EmailField(_('email address'), unique=True, null=True, max_length=200)
    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
