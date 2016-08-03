from django.db import models


class Users(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    user = models.CharField()
    password = models.CharField()
    email = models.CharField()
    active = models.IntegerField()
