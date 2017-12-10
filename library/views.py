# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from library.models import Book

# Create your views here.
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from library.models import Book
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', locals())


def list_of_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'list.html', locals())


# def genre_list(request, genre_id):
#     books = Book.objects.filter(Book, genre=genre_id)
#     return render(request, 'genre_list.html', locals())


def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book.html', {"book": book})


def sign_in(request):
    return render(request, 'sign_in.html', locals())

def add_like(request, book_id):
   book = get_object_or_404(Book, id=book_id)  # возвращает id статьи или 404.
   book.book_likes += 1 # Прибавляет единицу к article_likes
   book.save() # сохраняет
   return HttpResponseRedirect('/') # делает редирект на ту же страницу

# def addlike(request, book_id):
#     try:
#         if book_id in request.COOKIES:
#             redirect('/')
#         else:
#             book = Book.objects.get(id=book_id)
#             book.book_likes += 1
#             book.save()
#             response =  redirect('/')
#             response.set_cookie( book_id,"test")
#             return response
#     except ObjectDoesNotExist:
#         raise Http404
#     return redirect('/')

# def add_like(request, slug):
#     try:
#         book = get_object_or_404(Book, slug=slug)
#         book.book_likes += 1
#         book.save()
#     except ObjectDoesNotExist:
#         return Http404


# def registration(request):
#     return render(request, 'registration.html', locals())
#
# def registration(request):
#     return render(request, 'comments.html', locals())

