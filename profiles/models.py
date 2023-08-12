from django.db import models
from accounts.models import User


class Journalist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='journalist')

    def __str__(self):
        return self.user.get_full_name()


class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor')

    def __str__(self):
        return self.user.get_full_name()
