from django.contrib import admin
from .models import AuthorsModel


@admin.register(AuthorsModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'pseudo_name', 'age', 'birth_date')
    search_fields = ('name', 'surname', 'pseudo_name', 'age')
    list_filter = ("name",)