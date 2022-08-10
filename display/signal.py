from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from display.models import profile
from display.models import Blog


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()