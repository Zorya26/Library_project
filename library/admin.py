# -*- coding: utf-8 -*-
from django.contrib import admin
from library.models import Book, Comments
# Register your models here.


class BookInline(admin.StackedInline):
    model = Comments
    extra = 2


class BookAdmin(admin.ModelAdmin):
    fields = ['id', 'book_title', 'book_image', 'book_author', 'book_year', 'book_genre', 'book_description', 'book_text', 'book_likes']
    list_display = ('id', 'book_title', 'book_author', 'book_genre', 'bit', 'book_text', 'book_likes')
    inlines = [BookInline]
    list_filter = ['book_genre']


admin.site.register(Book, BookAdmin)
