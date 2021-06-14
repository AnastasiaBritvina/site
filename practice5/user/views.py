from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth import authenticate, login
from .forms import ConsultationForm, ApplicationForm, LoginForm, UserRegistrationForm
from django.views.generic import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from .models import Application
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib.auth.views import LogoutView
from django.views import View


class ProfileActive():
    u = 13
    def __init__(self,user):
        self.user_active = user

def accountOfUser(request):
    return render(request, 'user/usersAccount.html')


def sendOfConsForm(request):
    return render(request, 'user/sendOfConsForm.html')


def sendOfAppForm(request):
    return render(request, 'user/sendOfAppForm.html')

def user_login_before_app(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/applicationForm')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'user/loginForApp.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/account_view')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

def user_login(request): # Получает  id пользователя
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.is_active:
                        current_user = request.user
                        print(current_user.id)

                        ProfileActive.u = int(current_user.id)
                        print('000000000000000000000000000')
                        print(ProfileActive.u)


                    return HttpResponseRedirect('/account_view')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

def register(request): # регистрация с занесением в группу клиенты
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_user.groups.add(Group.objects.get(name='clients'))
            # new_user.groups.add(Group.objects.get(name='staff'))

            return render(request, 'user/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'user_form': user_form})

def register_before_app(request): # регистрация с занесением в группу клиенты
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_user.groups.add(Group.objects.get(name='clients'))
            # new_user.groups.add(Group.objects.get(name='staff'))

            return render(request, 'user/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/registerForApp.html', {'user_form': user_form})

# def register(request): # старая регистрация
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return render(request, 'user/register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'user/register.html', {'user_form': user_form})

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

def account_view(request):
    # application = Application()
    # application_id = application.get_application_id(request)
    # items_in_application = ApplicationItems.objects.filter(application_id=application_id)

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/register')

    if request.user.is_staff:
        template = 'staff/managersAccount.html'
    else:
        template = 'user/usersAccount.html'

    product = Application.objects.get(user=User.objects.get(pk=ProfileActive.u))  # надо узнать id авторизованного клиента

    INFO = {
        'nameOfClient': product.nameOfClient,
        # 'emailOfClient': product.emailOfClient,
        'kindOfEvent': product.kindOfEvent,
        'phoneOfClient': product.phoneOfClient,
        'purposeOfEvent': product.purposeOfEvent,
        'dateTimeOfEvent': product.dateTimeOfEvent,
        'budgetOfEvent': product.budgetOfEvent,
        'placeOfEvent': product.placeOfEvent,
        'numberOfGuests': product.numberOfGuests,
        'ageOfGuests': product.ageOfGuests,
        'periodOfPreparation': product.periodOfPreparation,
        'addInfo': product.addInfo,
        'newInfo': product.newInfo,
    }
    contex = {}
    contex.update(INFO)


    return render(request, template, contex)

# def submit(request):
#     newInfo = request.GET['newInfo']
#     newInfo.save()
#     myList = {"newInfo": newInfo
#               }
#     return render(request, 'user/userAccount.html', context=myList)
#
# def list(request):
#     myList = {"allToDo": Stroka.objects.all()
#               }
#     return render(request, 'user/userAccount.html', context=myList)

# class ClientsProfile(View):
#   #  model = Application
#     template_name = 'user/usersAccount.html'
#  #   context_object_name = 'application'
#
#     def get(self, request):
#         product = Application.objects.get(user=User.objects.get(pk=ProfileActive.u))  # надо узнать id авторизованного клиента
#
#
#         INFO = {
#              'kindOfEvent': product.kindOfEvent,
#              'phoneOfClient': product.phoneOfClient,
#              'email': 'test@vegefood.ru'
#         }
#         contex = {}
#         contex.update(INFO)
#
#         print(contex)
#
#
#         return render(request, template_name, contex)









