from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

class Consultation(models.Model):
    nameOfGuest = models.CharField(max_length=300)
    question = models.TextField()
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)


class Application(models.Model):
    nameOfClient = models.CharField(max_length=300)
    phoneOfClient = models.CharField(max_length=300)
    kindOfEvent = models.TextField()
    purposeOfEvent = models.TextField()
    dateTimeOfEvent = models.CharField(max_length=300)
    budgetOfEvent = models.CharField(max_length=300)
    placeOfEvent = models.CharField(max_length=1000)
    numberOfGuests = models.CharField(max_length=300)
    ageOfGuests = models.CharField(max_length=300)
    periodOfPreparation = models.TextField()
    addInfo = models.TextField()
    findOut = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name = 'user', on_delete = models.CASCADE)

    def __str__(self):
        return self.nameOfClient

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwarge):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwarge):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
