from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import info
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'finalweb.html')
    else:
        return redirect('/special_app/signup')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('signin.html')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signup_output(request):
    userdata = info(Username=request.POST.get('username'), Email=request.POST.get('email'),
                    Password=request.POST.get('password'),
                    Firstname=request.POST.get('firstname'), Lastname=request.POST.get('lastname'),
                    Age=request.POST.get('age'),
                    Date_Of_Birth=request.POST.get('birthdate'), Gender=request.POST.get('gender'))
    userdata.save()
    str1 = "Hi", + str(userdata.Firstname) + "you registered into our website successfully.."
    return render(request, "signin.html", {'msg': str1})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/special_app/finalweb.html')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
