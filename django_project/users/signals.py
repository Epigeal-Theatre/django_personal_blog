from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signal to automatically create a Profile whenever a new User is created.
@receiver(post_save, sender=User)  # Connect the post_save signal to this function for the User model.
def create_profile(sender, instance, created, **kwargs):
    if created:  # If a new user is created, create a corresponding Profile.
        Profile.objects.create(user=instance)

# Signal to save the Profile whenever the User instance is saved.
@receiver(post_save, sender=User)  # Connect the post_save signal to this function for the User model.
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # Save the related Profile whenever the User is saved.
