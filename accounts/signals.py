from django.db.models.signals import post_save
from .models import CustomUser, Profile
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()