from .models import Feedback
from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select


class FeedbackForm(ModelForm):
    guest = forms.CharField(label='Ваше имя')

    class Meta:
        model = Feedback
        fields = ['guest', 'body', 'category']

        widgete = {
            "guest": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
        }