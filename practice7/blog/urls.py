from django.urls import path
from .views import BlogListView
from django.views.generic import DetailView
from blog.models import Blog

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<int:pk>', DetailView.as_view(model=Blog, template_name="blog/single.html")),
]