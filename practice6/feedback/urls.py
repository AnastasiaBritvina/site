from django.urls import path
from . import views
from feedback.views import FBListView

urlpatterns = [
    path('', FBListView.as_view(), name='feedback'),
    path('createFB', views.createFB, name='createFB'),

]
