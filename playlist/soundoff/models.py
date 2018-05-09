from django.db import models

class User(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)

class Playlist(models.Model):
  username = models.CharField(max_length=50)
  playname = models.CharField(max_length=150)
  songname = models.CharField(max_length=150)
