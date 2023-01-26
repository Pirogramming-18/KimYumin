from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
path('',post_list),
path('admin/', admin.site.urls),
path('like_ajax/',like_ajax),

]