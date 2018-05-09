from django.shortcuts import render
from django.http import HttpResponse
from login.models import User, Playlist
from login.serializers import UserSerializer, PlaylistSerializer
from rest_framework import generics

def homepage(request):
    return HttpResponse("Placeholder to be updated!!!!!")
