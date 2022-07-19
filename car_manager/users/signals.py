from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail

from users.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
        send_mail(
            "Welcome to Car Manager",
            "Welcome! I'm happy you're here!",
            "",
            [f"{instance.email}"],
            fail_silently=False,
        )