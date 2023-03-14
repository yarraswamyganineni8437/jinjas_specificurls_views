from django.shortcuts import render

# Create your views here.
def telugusongs(request):
    d={'singer':'karthik','femalesinger':'ks_chitra'}
    return render(request,'music_htmlpage.html',context=d)

def hindisongs(request):
    d={'singer1':'sonunigam','singer2':'shreyagoshal'}
    return render(request,'music2_htmlpage.html',context=d)
