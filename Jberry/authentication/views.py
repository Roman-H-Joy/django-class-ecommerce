from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_log, authenticate, logout as auth_logout
# from .models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # print(name, email, password)
        exists = User.objects.filter(email=email).first()
        if exists is None:
            user = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return render(request, 'login.html', {'success': 'Congratulations ...! You are Successfully registered and you are now new member'})
        else:
            return render(request, 'register.html', {'error': 'Oops ! You have already registered account using '+email+' this email address .'})
    return render(request, 'register.html', {'path': request.path})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(
            request=request, username=username, password=password
        )
        print(bool(user))
        if user is not None:
            auth_log(request, user)
            request.session['user'] = user.id
            return redirect('index')
        else:
            return render(request, 'login.html', {'credentialerror': 'Opps ! Your Given Credential is Incorrect ...'})
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    request.session['user'] = 0
    return redirect('login')

# This Line only for debugging purpose ......
