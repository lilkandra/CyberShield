from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('/log_in')
    else:
        return render(request, 'log_in.html')
    

def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2 and len(password)>4:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists!')
                return redirect('/sign_up')
            elif len(email)==0 or len(username)==0:
                messages.info(request, 'all fields are obligatory!')
                return redirect('/sign_up')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists!')
                return redirect('/sign_up')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
                return redirect('/log_in')
        else:
            messages.info(request, 'password is not the same!')
            return redirect('/sign_up')
    else:
        return render(request, 'sign_up.html')
    
def log_out(request):
    logout(request)
    return redirect('/')

def help(request):
    return render(request, 'help.html')

def dashboard(request):
    return render(request, 'dashboard1.html')

