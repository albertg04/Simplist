from django.db import models

# Create your models here.
class Users(models.Model):
    spotify_id = models.IntegerField();