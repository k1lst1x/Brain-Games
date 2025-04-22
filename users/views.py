from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.score = 0
            user.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('users:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
