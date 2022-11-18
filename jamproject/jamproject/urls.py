from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from jamapp import views
from jamapp.views import SongViewSet, AlbumViewSet, GenreViewSet, PlaylistViewSet

router = routers.DefaultRouter()
router.register(r'Songs', views.SongViewSet)
router.register(r'Albums', views.AlbumViewSet)
router.register(r'Genres', views.GenreViewSet)
router.register(r'Playlists', views.PlaylistViewSet)

Song_list = SongViewSet.as_view({
    'get': 'list'
})

Album_list = AlbumViewSet.as_view({
    'get': 'list'
})

Genre_list = GenreViewSet.as_view({
    'get': 'list'
})

Playlist_list = PlaylistViewSet.as_view({
    'get': 'list'
})


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('songs', Song_list, name='song-list'),
    path('albums', Album_list, name='album-list'),
    path('genres', Genre_list, name='song-list'),
    path('playlist', Playlist_list, name='playlist-list'),
]