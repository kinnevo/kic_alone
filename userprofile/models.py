from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bio', 'location',)

def save_profile(backend, user, response, *args, **kwargs):
#    print "SAVE"
    if backend.name == 'facebook':
#        print "backend facebook"
        profile = Profile.objects.get(pk=user.id)

        if profile is None:
            profile = Profile(user_id=user.id)
#        else:
#            print "Profile", profile
#        print "Email: ", response.get('email')
#        print "user obj: ", user

        profile.email = response.get('email')

#        profile.gender = response.get('gender')
#        profile.link = response.get('link')
#        profile.timezone = response.get('timezone')
#        print "profile: ", profile
        profile.save()