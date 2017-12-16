# -*- coding: utf-8 -*-
from django.contrib import admin
from library.models import Book, Comments
# Register your models here.


class BookInline(admin.StackedInline):
    model = Comments
    extra = 2


class BookAdmin(admin.ModelAdmin):
    fields = ['book_title', 'book_image', 'book_author', 'book_year', 'book_genre', 'book_description', 'book_text', 'book_pages', 'book_lang', 'book_lang_origin', 'book_trans', 'book_publisher', 'book_publisher_city']
    list_display = ('book_title', 'book_author', 'book_genre', 'bit', 'book_text', 'book_likes', 'book_pages', 'book_lang', 'book_lang_origin', 'book_trans', 'book_publisher', 'book_publisher_city', 'book_dislikes',)
    inlines = [BookInline]
    list_filter = ['book_genre']


admin.site.register(Book, BookAdmin)
