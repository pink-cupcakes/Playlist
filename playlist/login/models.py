from django_mysql.models import JSONField, Model
from django.db import models

class User(models.Model):
  username      = models.CharField(max_length=50, unique=True)
  password      = models.CharField(max_length=50)

  def __str__(self):
    return self.username

class Playlist(models.Model):
  user          = models.ForeignKey(User, on_delete=models.CASCADE)
  playlist_name = models.CharField(max_length=150)

  def __str__(self):
    return self.playlist_name

class Song(models.Model):
  playlist      = models.ForeignKey(Playlist, on_delete=models.CASCADE)
  song_name     = models.CharField(max_length=150)

  def __str__(self):
    return self.song_name


