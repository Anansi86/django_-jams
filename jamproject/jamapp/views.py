from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Song, Album, Genre, Playlist, Artist
from .serializers import SongSerializer, AlbumSerializer, GenreSerializer, PlaylistSerializer, ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all().order_by("title")

class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all().order_by("title")

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by("type")

class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all().order_by("created")
    
    @action(detail=True, methods=['post'])
    def add_song(self, request, pk=None):
        song = Song.objects.get(pk=request.data["song_id"])
        playlist = Playlist.objects.get(pk=pk)
        playlist.songs.add(song)
        playlist.Total_songs = playlist.songs.count()  #<how 
        playlist.save()
        return Response({'success': True})

class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Playlist.objects.all().order_by("name")