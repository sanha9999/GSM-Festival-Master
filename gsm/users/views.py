from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def sign_up_view(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')

        user = User.objects.create_user(username, password, confirm)
        user.name = name
        user.save()
        return redirect('sign_in')
    return render(request, "users/sign-up.html")

def main_view(request):
    return render(request, "users/main.html")

def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
            return render(request, "users/index.html")
        else:
            print("인증 실패")
    return render(request, "users/sign-in.html")


def logout_view(request):
    logout(request)
    return redirect('sign_in')