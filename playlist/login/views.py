from django.shortcuts import render
from django.http import HttpResponse
from login.models import User, Playlist
from login.serializers import UserSerializer, PlaylistSerializer
from rest_framework import generics

def homepage(request):
    return HttpResponse("Placeholder to be updated!!!!!")

def userpage(request, username):
    playlists = Playlist.objects.filter(user=username)
    innerHTML = ''

    for playlist in playlists:
        url = '/username=' + str(username) + '/' + str(playlist.pk)
        innerHTML += '<a href="' + url + '">' + playlist.playlist_name + '</a><br>'

    return HttpResponse(innerHTML)

def playlist(request, username, playlist):
    return HttpResponse("Songs will go here")