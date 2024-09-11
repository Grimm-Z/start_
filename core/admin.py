from django.contrib import admin
from .models import *

admin.site.register(Ticket)
admin.site.register(Additional)
admin.site.register(Ticket_buy)