from django.contrib.auth.models import User
from django.urls import path
from . import views
from staff.views import ClientsListView
from django.views.generic import DetailView

urlpatterns = [
    path('managersAccount/', views.managersAccount, name='managersAccount'),
    path('baseOfClients/', ClientsListView.as_view(), name='user'),
    path('<int:pk>', DetailView.as_view(model=User, template_name="staff/aboutClient.html")),
]