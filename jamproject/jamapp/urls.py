from djang.urls import path
from .views import JamappView

urlpatterns = {
    path('jamapp/', JamappView.as_view()),
    path('jamapp/<str:pk>', JamappView.as_view())
}