from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q #search
# Create your views here.
def Detail(request,id):
    houses = House.objects.get(id=id)
    userprofil = userProfil.objects.get(user = request.user.id)
    
    
    context={
        "houses":houses,
        "userprofil":userprofil,
    }
    return render(request,'detail.html',context)

def anaSayfa(request):
    houses=House.objects.all()
    
    context={
        'houses':houses,
    }
            
    return render(request, 'anasayfa.html', context)

def girisYap(request):
    if 'login' in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect('anaSayfa')

def Kayit(request):
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            user = User.objects.create_user(first_name=name, last_name=surname, email=email, username=username, password=password1)
            user.save()
        print(request.POST)
    return redirect('anaSayfa')


def Detay(request):
    return render(request, 'detay.html')
def Profil(request):
    return render(request, 'user/profil.html')
