from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# Signin
def signin(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'],
            password = request.POST['password'])
            auth.login(request,user)
            return redirect('/')
    return render(request, 'account/signin.html')


# Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'account/login.html',{'error': 'username or password is not correct please try again'})
    else:
        return render(request,'account/login.html')


# Logout

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    
    return render(request, 'account/login.html')


