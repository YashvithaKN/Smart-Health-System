from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
       

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
        

    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def delete_profile(request):
    user = request.user
    if request.method == "POST":
        user.delete()
        logout(request)  # log out after deletion
        return redirect('accounts:register')
    return render(request, 'accounts/delete_profile.html')