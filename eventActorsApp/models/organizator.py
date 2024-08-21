from django.db import models
from authApp.models import User

import uuid


class Organizator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nit = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=150)
    telephone = models.CharField(max_length=15)
    contact_email = models.EmailField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
