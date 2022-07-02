from django.db import models

# Create your models here.

class Task (models.Model):
    sno = models.BigIntegerField(primary_key=True)
    task = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
