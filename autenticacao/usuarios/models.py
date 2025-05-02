from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)  # estudante ou professor

    def __str__(self):
        return f"{self.user.email} ({self.tipo})"


# Create your models here.
