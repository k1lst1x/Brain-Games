from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    score = models.PositiveIntegerField(_('Очки'), default=0)

    def __str__(self):
        return self.username
