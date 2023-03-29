from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q #search
# Create your views here.

def anaSayfa(request):
    return render(request, 'anasayfa.html')

def girisYap(request):
    return render(request, 'user/girisyap.html')

def Kayıt(request):
    return render(request, 'user/kaydol.html')
def Detay(request):
    return render(request, 'detay.html')

