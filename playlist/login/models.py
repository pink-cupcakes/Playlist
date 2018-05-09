from django.db import models

class User(models.Model):
  username      = models.CharField(max_length=50, primary_key=True)
  password      = models.CharField(max_length=50)

  def __str__(self):
    return self.pk

class Playlist(models.Model):
  user          = models.ForeignKey(User, on_delete=models.CASCADE)
  playlist_name = models.CharField(max_length=150)

class Song(models.Model):
  playlist_id   = models.ForeignKey(Playlist, on_delete=models.CASCADE)
  song_name     = models.CharField(max_length=150)


