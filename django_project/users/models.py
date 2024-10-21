from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Profile model to store additional user information, specifically their profile image.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links each profile to one user (one-to-one relationship).
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # Stores profile image with a default image and upload location.

    def __str__(self):
        return f'{self.user.username} Profile'  # Displays the profile as the user's username followed by "Profile".

    # Override the save method to resize images before saving.
    def save(self, *args, **kwargs):
        # Call the parent class's save method to save the model first.
        super().save(*args, **kwargs)

        # Open the uploaded image using PIL.
        img = Image.open(self.image.path)

        # Check if the image dimensions exceed 300x300 pixels.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize the image while maintaining aspect ratio.
            img.save(self.image.path)  # Save the resized image back to the same path.


