from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

def managersAccount(request):
    return render(request, 'staff/managersAccount.html')

class ClientsListView(ListView):
    model = User
    template_name = 'staff/baseOfClients.html'
    context_object_name = 'user'
