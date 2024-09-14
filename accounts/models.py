from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    display_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.display_name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.display_name}'

    class Meta:
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzern'