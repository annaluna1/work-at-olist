from django.contrib import admin
from .models import Authors, Books


# Register your models here.

class AuthorsDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'authors_name']


class BooksDetailAdmin(admin.ModelAdmin):
    model = Authors
    list_display = ['id', 'book_name', 'book_edition', 'book_year', 'book_author']

    def get_name(self, obj):
        return obj.book_author.authors_name

    get_name.short_description = 'book_author'


admin.site.register(Authors, AuthorsDetailAdmin)
admin.site.register(Books, BooksDetailAdmin)
