from django.urls import path,include
from .views import review_update,review_delete,review_details,review_create,review_list
urlpatterns = [
    path('',review_list),
    path('review/<int:pk>',review_details),
    path('review/create',review_create),
    path('review/<int:pk>/update',review_update),
    path('review/<int:pk>/delete',review_delete),
]
