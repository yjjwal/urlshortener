from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from urlshortner.middleware import auth,guest
from shortner.models import ShortURL
from django.contrib import messages

# Create your views here.
@guest
def register_views(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Successfully registored!!")
            return redirect('dashboard')
        else:
            messages.error(request,"Registration is Failed!!")

    else:
        form = UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
@guest
def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"Successfully logedin!!")
            return redirect('dashboard')
        else:
            messages.error(request,"Login failed!!")

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
def logout_views(request):
    logout(request)
    return redirect('login')
@auth
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user)
    return render(request,'accounts/dashboard.html',{'urls':urls})


