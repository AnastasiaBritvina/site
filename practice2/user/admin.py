from django.contrib import admin
from user.models import Consultation
from user.models import Application

admin.site.register(Consultation)
admin.site.register(Application)
