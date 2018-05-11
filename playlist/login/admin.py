from django.contrib import admin
from .models import User, Playlist, Song

admin.site.register(User)
admin.site.register(Playlist)
admin.site.register(Song)