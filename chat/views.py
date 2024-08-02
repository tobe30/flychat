from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'mood/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already exist')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username Already exist')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            return redirect('signin')
    else:                  
      return render(request, 'mood/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('message:index')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')
    else:
     return render(request, 'mood/signin.html')
