from django.urls import path
from . import views
from user.models import Application


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
    # path('submit/account_view', views.submit, name='submit'),
    # path('<int:id>', views.list, name='list'),
    # path('appOfClient/', views.appOfClient, name='appOfClient'),
    # path('find/<client_name>', ForClientsProfile.as_view()),
]