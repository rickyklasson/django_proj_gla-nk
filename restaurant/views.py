from django.shortcuts import render
from .models import MenuEntry, Review


def index(request):
    # A la carté
    förrätter = MenuEntry.objects.all().filter(category__name__iexact='förrätter')
    varmrätter = MenuEntry.objects.all().filter(category__name__iexact='varmrätter')
    schnitzel = MenuEntry.objects.all().filter(category__name__icontains='schnitzel')
    desserter = MenuEntry.objects.all().filter(category__name__iexact='desserter')

    a_la_carte = {'förrätter': förrätter,
                  'varmrätter': varmrätter,
                  'schnitzelkavalkad': schnitzel,
                  'desserter': desserter}

    # Dryck
    fördrinkar = MenuEntry.objects.all().filter(category__name__iexact='fördrinkar')
    röda_viner = MenuEntry.objects.all().filter(category__name__iexact='röda viner')
    vita_viner = MenuEntry.objects.all().filter(category__name__iexact='vita viner')
    

    dryck_flags = [0, 1, 0, 0]
    dryck = {'fördrinkar': fördrinkar,
             'viner': {'vita viner': vita_viner, 'röda viner': röda_viner}}

    # Guestbook
    guest_book = Review.objects.all()

    context = {'a_la_carte': a_la_carte,
               'dryck': dryck,
               'dryck_flags': dryck_flags,
               'guest_book': guest_book}

    return render(request, 'base.html', context=context)
