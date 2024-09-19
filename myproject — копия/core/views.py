from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket_buy, Ticket

def home(request):
    return render(request, 'reservations/home.html')

def booking_form(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()     
            return redirect('success')
    else:
        form = TicketForm()
    return render(request, 'reservations/ticket_form.html', {'form': form})

def success(request):
    return render(request, 'reservations/success.html')

def list(request):
    return render(request, 'reservations/list_of.html')