from django.db import models
from djangotoolbox.fields import ListField



class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()



class Measure(models.Model):
    sensor = models.CharField()
    type = models.IntegerField()
    value = models.FloatField()
    fecha = models.CharField()




class Users(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    user = models.CharField()
    password = models.CharField()
    email = models.CharField()
    active = models.IntegerField()
