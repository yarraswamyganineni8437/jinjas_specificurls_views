from django.urls import path
from movies.views import *
app_name='something'

urlpatterns=[
    path('telugumovies/',telugumovies,name='telugumovies'),
    path('hindimovies/',hindimovies,name='hindimovies'),
]