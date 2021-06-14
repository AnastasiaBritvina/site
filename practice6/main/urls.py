from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('potfolio/photosFromEvents/', views.photosFromEvents, name='photosFromEvents'),
    path('potfolio/clientsAndPartners/', views.clientsAndPartners, name='clientsAndPartners'),
    path('serverses/typesOfServerses/', views.typesOfServerses, name='typesOfServerses'),
    path('serverses/additionalServices/', views.additionalServices, name='additionalServices'),
]
