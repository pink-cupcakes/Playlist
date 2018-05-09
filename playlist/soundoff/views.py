from django.shortcuts import render
from django.http import HttpResponse
from soundoff.models import User, Playlist
from soundoff.serializers import UserSerializer, PlaylistSerializer
from rest_framework import generics

def login(request):
    return HttpResponse("Placeholder to be updated!!!!!")
