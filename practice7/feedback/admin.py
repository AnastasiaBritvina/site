from django.contrib import admin
from feedback.models import Feedback
from feedback.models import CategoryOfFB

admin.site.register(Feedback)
admin.site.register(CategoryOfFB)