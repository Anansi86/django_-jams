from django.contrib import admin
from .models import Song, Album, Genre, Playlist

class SongAdmin(admin.ModelAdmin):
    pass
admin.site.register(Song, SongAdmin)

class AlbumAdmin(admin.ModelAdmin):
    pass
admin.site.register(Album, AlbumAdmin)

class GenreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre, GenreAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Playlist, PlaylistAdmin)

