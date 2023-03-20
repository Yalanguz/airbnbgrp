from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q #search
# Create your views here.
