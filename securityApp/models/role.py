from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
