from tkinter import Menu
from django.shortcuts import render
from .models import MenuEntry, Review

# Create your views here.


def index(request):
    starters = MenuEntry.objects.filter(
        menu_category__menu_category__icontains='Förrätter')
    main_courses = MenuEntry.objects.filter(
        menu_category__menu_category__icontains='Varmrätter')

    guest_book = Review.objects.all()

    context = {'starters': starters,
               'main_courses': main_courses,
               'guest_book': guest_book}

    return render(request, 'base.html', context=context)
