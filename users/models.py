from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
