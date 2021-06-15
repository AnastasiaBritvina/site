from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    paginate_by = 2
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

