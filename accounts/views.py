from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def signup(request):
    # Function for signing up using a custom form that uses djangos built in auth system.
    # It logs you in automatically upon success and redirects you to the Kix school schedule.
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('stacktry:bjj_lesson_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
