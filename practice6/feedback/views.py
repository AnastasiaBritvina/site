from django.shortcuts import render, redirect
from django.views.generic import ListView
from feedback.models import Feedback
from .forms import FeedbackForm


class FBListView(ListView):
    model = Feedback
    paginate_by = 2
    template_name = 'feedback/feedback.html'
    context_object_name = 'feedback'

def createFB(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/feedback')
        else:
            error = "Ошибка валидации"
    form = FeedbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'feedback/createFB.html', data)