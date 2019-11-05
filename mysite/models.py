from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver


class User_from_my_db(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, default=1)
    street = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=4, blank=True)
    plz = models.PositiveIntegerField(blank=True, default=1, null=True)
    city = models.CharField(max_length=50, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_from_my_db.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

