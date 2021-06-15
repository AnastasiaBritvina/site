from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

# def managersAccount(request):
#     return render(request, 'staff/managersAccount.html')

class ClientsListView(ListView):
    model = User
    template_name = 'staff/baseOfClients.html'
    context_object_name = 'user'

    def get_success_url(self):
        print(self.request)
        return reverse_lazy('accounts:list_messages', kwargs={'uname': self.request.user.username })

