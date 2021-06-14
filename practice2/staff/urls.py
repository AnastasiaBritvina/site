from django.urls import path
from . import views
from staff.views import ClientsListView

urlpatterns = [
    path('managersAccount/', views.managersAccount, name='managersAccount'),
    path('baseOfClients/', ClientsListView.as_view(), name='user'),
]