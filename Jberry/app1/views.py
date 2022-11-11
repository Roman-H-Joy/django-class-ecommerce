from django.shortcuts import render, HttpResponse
# from .models import User
# Create your views here.


def index(request):
    if request.session.get('user', None):
        user = request.user
        return render(request, 'index.html', {'user': user})
    return render(request, 'index.html', {'path': request.path})
