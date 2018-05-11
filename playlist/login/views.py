from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse
from login.models import User, Playlist, Song
from login.serializers import UserSerializer, PlaylistSerializer
from rest_framework import generics

def homepage(request):
    return render(request, 'login/index.html')

def userpage(request, username):
    current_user  = get_object_or_404(User, username=username)
    playlists = get_list_or_404(Playlist, user_id=current_user.id)

    return render(request, 'login/list.html', {'playlists': playlists, 'username': username})

def playlist(request, username, playlist):
    current_user  = get_object_or_404(User, username=username)
    user_playlist = get_object_or_404(Playlist, user_id=current_user.id, pk=playlist)
    songs = Song.objects.filter(pk=playlist)

    return render(request, 'login/item.html', {'songs': songs, 'user_playlist': user_playlist})