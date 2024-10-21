from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# View for user registration
def register(request):
    if request.method == 'POST':  # If the form is submitted via POST
        form = UserRegisterForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Validate the form
            form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')  # Get the username from the form
            messages.success(request, f'Your account has been created! You are now able to log in.')  # Success message
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()  # If not POST, create an empty form for a GET request
    return render(request, 'users/register.html', {'form': form})  # Render the registration page with the form


# View for updating user profile (requires login)
@login_required
def profile(request):
    if request.method == 'POST':  # If the form is submitted via POST
        u_form = UserUpdateForm(request.POST, instance=request.user)  # Form to update user details
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # Form to update profile

        if u_form.is_valid() and p_form.is_valid():  # Validate both forms
            u_form.save()  # Save updated user data
            p_form.save()  # Save updated profile data
            messages.success(request, f'Your account has been updated!')  # Success message
            return redirect('profile')  # Redirect to the profile page after saving changes
    else:
        u_form = UserUpdateForm(instance=request.user)  # Populate the form with the user's current data for GET
        p_form = ProfileUpdateForm(instance=request.user.profile)  # Populate the profile form with current profile data

    context = {
        'u_form': u_form,  # Pass the user update form to the template
        'p_form': p_form   # Pass the profile update form to the template
    }

    return render(request, 'users/profile.html', context)  # Render the profile page with both forms


