from django.shortcuts import render

# Create your views here.
def telugumovies(request):
    d={'movie1':'premikularoju','movie2':'oye!'}
    return render(request,'movie_htmlpage.html',context=d)

def hindimovies(request):
    d={'movie1':'Aashique2','movie2':'dhadak'}
    return render(request,'movie2_htmlpage.html',context=d)