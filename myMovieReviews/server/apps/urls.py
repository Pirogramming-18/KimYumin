from django.urls import path,include
from server.apps.views import movie_list
urlpatterns = [
    path('/',movie_list)
]
