from .models import Consultation, Application
from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


class ConsultationForm(ModelForm):
    nameOfGuest = forms.CharField(label='Ваше имя/наименование')
    question = forms.CharField(label='Введите ваш вопрос')
    email = forms.CharField(label='e-mail')
    phone = forms.CharField(label='Телефон')

    class Meta:
        model = Consultation
        fields = ['nameOfGuest', 'question', 'email', 'phone']

        widgete = {
            "nameOfGuest": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя/наименование'
            }),
            "question": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш вопрос'
            }),
            "minuses": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Минусы'
            }),
            "email": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'e-mail'
            }),
            "phone": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш телефон'
            }),
        }


class ApplicationForm(ModelForm):
    nameOfClient = forms.CharField(label='Ваше имя/наименование')
    phoneOfClient = forms.CharField(label='Ваш номер телефона')
    kindOfEvent = forms.CharField(label='Что нужно организовать?')
    purposeOfEvent = forms.CharField(label='Цель мероприятия')
    dateTimeOfEvent = forms.CharField(label='Дата и время мероприятия')
    budgetOfEvent = forms.CharField(label='Планируемый бюджет')
    placeOfEvent = forms.CharField(label='Предполагаемое место проведения')
    numberOfGuests = forms.CharField(label='Количество присутствующих')
    ageOfGuests = forms.CharField(label='Средний возраст присутствующих')
    periodOfPreparation = forms.CharField(label='Сроки подготовки')
    addInfo = forms.CharField(label='Дополнительная информация')
    findOut = forms.CharField(label='Как вы узнали о нас?')

    class Meta:
        model = Application
        fields = ['nameOfClient', 'phoneOfClient', 'kindOfEvent',
                  'purposeOfEvent', 'dateTimeOfEvent', 'budgetOfEvent', 'placeOfEvent',
                  'numberOfGuests', 'ageOfGuests', 'periodOfPreparation', 'addInfo', 'findOut', 'user']

        widgete = {
            "nameOfClient": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя/наименование'
            }),
            "phoneOfClient": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "kindOfEvent": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Что нужно организовать?'
            }),
            "purposeOfEvent": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Цель мероприятия'
            }),
            "dateTimeOfEvent": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время мероприятия'
            }),
            "budgetOfEvent": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Планируемый бюджет'
            }),
            "placeOfEvent": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Предполагаемое место проведения'
            }),
            "numberOfGuests": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Количество присутствующих'
            }),
            "ageOfGuests": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Средний возраст присутствующих'
            }),
            "periodOfPreparation": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сроки подготовки'
            }),
            "addInfo": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительная информация'
            }),
            "findOut": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Как вы узнали о нас?'
            }),
            "user": Select(attrs={
                'class': 'form-control',
            }),
        }

