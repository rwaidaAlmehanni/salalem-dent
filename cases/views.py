from django.views import generic
from .models import Cases
from .forms import UserForm, CasesForm
from django.shortcuts import render, get_object_or_404
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
                return render(request, 'cases/index.html', {'cases': cases})
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

                return render(request, 'cases/detail.html', {'cases': cases})
            else:
                return render(request, 'cases/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'cases/login.html', {'error_message': 'Invalid login'})
    return render(request, 'cases/login.html')




def index(request):
    cases = Cases.objects.all()
    return render(request, 'cases/index.html', {'cases': cases})




def addCases(request):
    if not request.user.is_authenticated():
        return render(request, 'cases/addCases.html')
    else:
        form = CasesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            case = form.save(commit=False)
            case.description = request.POST['description']
            case.case_typ = request.POST['case_typ']
            case.owner = request.user.id
            case.save()
            return render(request, 'cases/detail.html', {'case': case})
        context = {
            "form": form,
        }
        return render(request, 'cases/addCases.html', context)



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'cases/login.html', context) 



def detail(request):
    if not request.user.is_authenticated():
        return render(request, 'cases/login.html')
    else:
        cases = Cases.objects.all()
    return render(request, 'cases/detail.html', {'cases':cases}) 



def delete_cases(request, cases_id):
    case = Cases.objects.get(pk=cases_id)
    case.delete()
    cases = Cases.objects.all()
    return render(request, 'cases/detail.html', {'cases': cases}) 


def my_cases(request):
    if not request.user.is_authenticated():
        return render(request, 'cases/login.html')
    else:
         cases = Cases.objects.filter(owner=request.user.id)
         return render(request, 'cases/my_cases.html', {'cases': cases})         









