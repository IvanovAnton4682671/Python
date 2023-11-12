
from django.db import models


class Users(models.Model):
    type = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=32)

