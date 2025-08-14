from django.shortcuts import render,redirect, get_object_or_404
from .models import Menu,Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu_view(request):
    menu_items = Menu.objects.all().order_by('name')  # Fetch all dishes sorted
    return render(request, 'menu.html', {'menu': menu_items})

def menu_item(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'item': item})

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'booking_success.html')
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})

from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def booking_list(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'booking_list.html', {'bookings': bookings})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after signup
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


