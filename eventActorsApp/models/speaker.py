from django.db import models

from authApp.models import User
from .organizator import Organizator
import uuid


class Speaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    organization = models.ForeignKey(Organizator, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
