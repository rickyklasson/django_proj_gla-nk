from tkinter import Menu
from django.shortcuts import render
from .models import MenuEntry

# Create your views here.


def index(request):
    menu_entries = MenuEntry.objects.all()

    return render(request, 'base.html', context={'menu_entries': menu_entries})
