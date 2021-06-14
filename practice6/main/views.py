from django.shortcuts import render


def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def photosFromEvents(request):
    return render(request, 'main/potfolio/photosFromEvents.html')

def clientsAndPartners(request):
    return render(request, 'main/potfolio/clientsAndPartners.html')

def typesOfServerses(request):
    return render(request, 'main/serverses/typesOfServerses.html')

def additionalServices(request):
    return render(request, 'main/serverses/additionalServices.html')