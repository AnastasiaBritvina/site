from django.urls import path
from . import views
from user.views import ClientsProfile
from user.models import Application

urlpatterns = [
    path('consultation', views.consultation, name='consultation'),
    path('applicationForm', views.application, name='applicationForm'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('usersAccount/', ClientsProfile.as_view(), name='application'),
    path('sendOfConsForm', views.sendOfConsForm, name='sendOfConsForm'),
    path('sendOfAppForm', views.sendOfAppForm, name='sendOfAppForm'),
    # path('find/<client_name>', ForClientsProfile.as_view()),
]