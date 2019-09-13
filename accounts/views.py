from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def check_user_login(user):
    return not user.is_authenticated

@user_passes_test(check_user_login, '/', None)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html' , {'form' : form })
