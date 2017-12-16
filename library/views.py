# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from library.models import Book

# Create your views here.
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from library.models import Book, Comments
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import CommentForm
from django.contrib import auth


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
    comments = Comments.objects.filter(comments_book=book_id)
    form_comment = CommentForm
    return render (request, 'book.html', {
        "book": book,
        "comments": comments,
        "form_comments": form_comment,
    })

def sign_in(request):
    return render(request, 'sign_in.html', locals())

def add_like(request, book_id):
    if book_id in request.COOKIES:
        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)
    else:
       book = get_object_or_404(Book, id=book_id)  # возвращает id статьи или 404.
       book.book_likes += 1 # Прибавляет единицу к article_likes
       book.save() # сохраняет
       return_path = request.META.get('HTTP_REFERER', '/')
       response = redirect(return_path)
       response.set_cookie (book_id, "test")
       return response # делает редирект на ту же страницу

def add_dislike(request, book_id):
    if book_id in request.COOKIES:
        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)
    else:
       book = get_object_or_404(Book, id=book_id)  # возвращает id статьи или 404.
       book.book_dislikes += 1  # Прибавляет единицу к article_likes
       book.save()  # сохраняет
       return_path = request.META.get('HTTP_REFERER', '/')
       response = redirect(return_path)
       response.set_cookie(book_id, "test")
       return response  # делает редирект на ту же страницу

def addcomment(request, book_id):
    if request.POST :
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.comments_author = request.user
            comment.comments_book = Book.objects.get(id=book_id)
            form.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            return response


# def registration(request):
#     return render(request, 'registration.html', locals())
#
# def registration(request):
#     return render(request, 'comments.html', locals())

# import re
# from django.db.models import Q
#
#
# def normalize_query(query_string,
#                     findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
#                     normspace=re.compile(r'\s{2,}').sub):
#     return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]
#
#
# def get_query(query_string, search_fields):
#     query = None  # Query to search for every search term
#     terms = normalize_query(query_string)
#     for term in terms:
#         or_query = None  # Query to search for a given term in each field
#         for field_name in search_fields:
#             q = Q(**{"%s__icontains" % field_name: term})
#             if or_query is None:
#                 or_query = q
#             else:
#                 or_query = or_query | q
#         if query is None:
#             query = or_query
#         else:
#             query = query & or_query
#     return query
#
#
# def search(request):
#     query_string = ''
#     found_entries = None
#     if ('q' in request.GET) and request.GET['q'].strip():
#         query_string = request.GET['q']
#
#         entry_query = get_query(query_string, ['title', 'body', ])
#
#         found_entries = Book.objects.filter(entry_query).order_by('-pub_date')
#
#     return render_to_response('base.html',
#                               {'query_string': query_string, 'found_entries': found_entries},
#                               context_instance=RequestContext(request))