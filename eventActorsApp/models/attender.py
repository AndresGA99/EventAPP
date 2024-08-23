from django.db import models
from authApp.models import User

import uuid


class Attender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    telephone = models.CharField(max_length=15)
    #city = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    