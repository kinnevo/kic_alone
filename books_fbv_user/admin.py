from django.contrib import admin
from models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'pages',
    )

admin.site.register(Book, BookAdmin)