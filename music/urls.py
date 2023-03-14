from django.urls import path
from music.views import *
app_name='nothing'
urlpatterns=[
    path('telugusongs/',telugusongs,name='telugusongs'),
    path('hindisongs/',hindisongs,name='hindisongs'),
]