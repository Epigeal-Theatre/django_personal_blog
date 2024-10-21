from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# This model represents a blog post in the application.
# Each post includes a title, content, a timestamp of when it was posted, 
# and a reference to the user who authored the post.

class Post(models.Model):
    # Title of the post, limited to 100 characters
    title = models.CharField(max_length=100)
    
    # Main content of the post, with no length restrictions
    content = models.TextField()
    
    # Date and time when the post was created, defaults to the current time
    # using timezone.now to handle time zone awareness.
    date_posted = models.DateTimeField(default=timezone.now)
    
    # ForeignKey establishes a many-to-one relationship with the User model.
    # When the author (User) is deleted, all their posts will also be deleted (CASCADE).
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # String representation of the Post model, used in the Django admin and shell.
    # Returns the title of the post.
    def __str__(self):
        return self.title

    # Returns the URL to the post's detail page.
    # 'post-detail' is the name of the URL pattern, and 'pk' is the primary key of the post.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





