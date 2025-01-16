from django.urls import path

from authors.views import all_authors

app_name = 'authors'

urlpatterns = [
    path('', all_authors, name='all_authors'),
]
