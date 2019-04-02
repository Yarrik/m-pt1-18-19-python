from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    user_name = "Oleg"
    return render(request, 'home/home.html', locals())

def cont(request):
    accounts = [
        ['Geralt', 'Kaer Morhen'],
        ['Yennefer', 'Vengerberg'],
        ['Cirilla', 'Cintra'],
        ['Crach an Craite', 'Skellige'],
        ['Dijkstra', 'Redania'],
        ['Reynart de Bois-Fresnes', 'Toussaint'],
    ]
    return render(request, 'home/contacts.html', locals())