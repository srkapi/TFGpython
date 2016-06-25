from django.db import models



class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()






class Users(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    user = models.CharField()
    password = models.CharField()
    email = models.CharField()
    active = models.IntegerField()
