from django import forms
from .models import Ticket_buy

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket_buy
        fields = ['user', 'ticket', 'start_date', 'end_date', 'status', 'additional_things',]