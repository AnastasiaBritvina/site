from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth import authenticate, login
from .forms import ConsultationForm, ApplicationForm, LoginForm, UserRegistrationForm
from django.views.generic import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from .models import Application


def accountOfUser(request):
    return render(request, 'user/usersAccount.html')


def sendOfConsForm(request):
    return render(request, 'user/sendOfConsForm.html')


def sendOfAppForm(request):
    return render(request, 'user/sendOfAppForm.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/usersAccount')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

# def user_login(request): # Получает  id пользователя
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     if request.user.is_active:
#                         current_user = request.user
#                         print(current_user.id)
#                     return HttpResponseRedirect('/usersAccount')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#         return render(request, 'user/login.html', {'form': form})




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'user/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'user_form': user_form})


def consultation(request):
    error = ''
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sendOfConsForm')
        else:
            error = "Ошибка валидации"
    form = ConsultationForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/consultation.html', data)


def application(request):
    error = ''
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sendOfAppForm')
        else:
            error = "Ошибка валидации"
    form = ApplicationForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/applicationForm.html', data)


# class ClientsProfile(ListView):
#     model = Application
#     template_name = "user/usersAccount.html"
#
#     def get_queryset(self):
#         self.username = get_object_or_404(User, username=self.kwargs['username'])
#         return Application.objects.filter(user__username=self.username)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['username'] = self.username
#         return context

# class ClientsProfile(ListView):
#     model = Application
#
#     template_name = 'user/usersAccount.html'
#     context_object_name = 'application'
#     product = Application.objects.get(user=User.objects.get(pk=2)) #надо узнать id авторизованного клиента
#     print(product.phoneOfClient)
#
#     INFO = {
#         'kindOfEvent': product.kindOfEvent,
#         'phone': product.phoneOfClient,
#         'email': 'test@vegefood.ru'
#      }



class ClientsProfile(ListView):
    model = Application
    template_name = 'user/usersAccount.html'
    context_object_name = 'application'

    def get_clients_profile(self, request):
        self.product = Application.objects.get(user=User.objects.get(pk=request.user.id))
        print(self.product.phoneOfClient)



# def user_login(request): # Получает  id пользователя
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     if request.user.is_authenticated:
#                         current_user = request.user
#                         print(current_user.id)
#                     return HttpResponseRedirect('/usersAccount')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#         return render(request, 'user/login.html', {'form': form})






