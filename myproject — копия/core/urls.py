from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('ticket/', views.booking_form, name = "ticket_form"),
    path('success/', views.success, name = "success"),
    path('list/', views.list, name = "list"),
]
