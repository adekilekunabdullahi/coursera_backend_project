# from django.http import HttpResponse
import genericpath
from django.shortcuts import render
from .forms import BookingForm, UserForms
from .models import Menu
from django.db import models
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from .serializer import UserSerializer
from django.contrib.auth import authenticate ,login 

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def registration(request):
    form = UserForms()
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():     
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            return render(request, 'menu.html')
    return render(request, 'registration.html', {'forms':form})

# def login
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             
#         else:
#             return HttpResponse('invalid user')


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')