from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Form for user registration, extending the default UserCreationForm to include an email field.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adding an email field, which is not included by default.

    class Meta:
        model = User  # User model is the target model for the form.
        fields = ['username', 'email', 'password1', 'password2']  # Fields to be displayed in the form.

# Form for updating user details like username and email.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # Email field for updating user email.

    class Meta:
        model = User  # The form updates the User model.
        fields = ['username', 'email']  # Fields for username and email updates.

# Form for updating the profile image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # Profile model contains user profile information.
        fields = ['image']  # Field to allow users to update their profile image.
