from django.views import generic
from .models import Cases
from .forms import UserForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                cases = Cases.objects.all()
                return render(request, 'cases/index.html', {'albums': cases})
    context = {
        "form": form,
    }
    return render(request, 'cases/signup.html', context)




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                cases = Cases.objects.all()
                return render(request, 'cases/index.html', {'albums': cases})
            else:
                return render(request, 'cases/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'cases/login.html', {'error_message': 'Invalid login'})
    return render(request, 'cases/login.html')










