from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Myuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Myuser.objects.create(user=instance)
        instance.myuser.save()

class Message(models.Model):
    Owner = models.CharField(max_length=63)
    Text = models.CharField(max_length=255)
    Date = models.DateField(auto_now=True)