from django.db import models

# Create your models here.
class StackFusion(models.Model):
    name = models.CharField(max_length=20)
    dateOfBirth=models.DateField()
    email = models.CharField(max_length=40)
    phone = models.IntegerField()