from django.contrib import admin
from .models import Author, Quote

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'user')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
