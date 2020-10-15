from django.contrib import admin
from .models import CurrencyRate

@admin.register(CurrencyRate)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'date',)
