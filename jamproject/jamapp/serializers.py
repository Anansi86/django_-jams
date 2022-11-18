#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Album, Genre, Playlist, Artist

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Album
        fields = "__all__"

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Playlist
        fields = "__all__"

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
