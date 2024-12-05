from django.shortcuts import render, redirect
from django.contrib import mess
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def userRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_vaild():
            form.save()
            username = form.cleanded_data.get('username')
            mess.success(request, f'Welcome to the Chat Room {username}!')
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {"form": form})

@login_required
def userpage(request):
    return(request, 'users/userpage.html')
