from django.urls import path
from . views import *
urlpatterns = [
    path('',IndexApiView.as_view(),name='index'),
    path('movies/',MovieApiView.as_view(),name='movies'),
     path('movies/review/<int:id>',ReviewAPIView.as_view(),name='reviews'),
]
