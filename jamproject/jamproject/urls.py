from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from jamapp import views
from jamapp.views import SongViewSet, AlbumViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register(r'Song', views.SongViewSet)
# router.register(r'groups', views.GroupViewSet)

song_list = SongViewSet.as_view({
    'get': 'list'
})

Album_list = AlbumViewSet.as_view({
    'get': 'list'
})

Genre_list = GenreViewSet.as_view({
    'get': 'list'
})


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('songs', song_list, name='song-list'),
    path('albums', Album_list, name='album-list'),
]