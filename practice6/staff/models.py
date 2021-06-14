from django.db import models
from user.models import Application

class Status(models.Model):
    title = models.CharField('название', max_length=50)
    created_et = models.DateTimeField(auto_now_add=True) #Для отметок времени
    application = models.ForeignKey(Application, related_name='application', on_delete=models.CASCADE)
