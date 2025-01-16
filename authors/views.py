from django.shortcuts import render

from .models import AuthorsModel


def all_authors(request):
    authors = AuthorsModel.objects.filter(age__gte=80) # bu yerda men 80 yoshdan katta bo'lgan authorlarni chiqardim!!!
    context = {
        'authors': authors
    }
    return render(request, 'index.html', context)