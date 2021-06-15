from django.urls import path
from . import views
from user.models import Application
from django.views.generic import DetailView
from .models import Application
# from user.views import LookAppOfClient



urlpatterns = [
    path('consultation', views.consultation, name='consultation'),
    path('applicationForm', views.application, name='applicationForm'),
    path('login', views.user_login, name='login'),
    path('loginForApp', views.user_login_before_app, name='loginForApp'),
    path('register', views.register, name='register'),
    path('registerForApp', views.register_before_app, name='registerForApp'),
    path('account_view', views.account_view, name='account_view'),
    path('sendOfConsForm', views.sendOfConsForm, name='sendOfConsForm'),
    path('sendOfAppForm', views.sendOfAppForm, name='sendOfAppForm'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('addStatus/', views.addStatus, name='addStatus'),
    # path('<int:pk>', DetailView.as_view(model=Application, template_name="staff/appOfClient.html")),
    path('appOfClient/<int:pk>', views.appOfClient, name='appOfClient'), # отображается только код страницы
    path('edit/', views.edit, name='edit'),
    path('update/', views.update, name='update')
    # path('usersAccount', views.list, name='list'),
    # path('appOfClient/<int:pk>', views.LookAppOfClient.as_view(), name='appOfClient'),
]

