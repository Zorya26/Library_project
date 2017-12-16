# -*- coding: utf-8 -*-
"""Library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from library import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/$', views.list_of_books, name='list'),
    # url(r'^list/(?P<genre_id>[0-9]+)/$', views.genre_list, name='genre_list'),
    url(r'^list/book/(?P<book_id>[0-9]+)/$', views.book, name='book'),
    url(r'^add_like/(?P<book_id>[0-9]+)/$', views.add_like, name='add_like'),
    url(r'^add_dislike/(?P<book_id>[0-9]+)/$', views.add_dislike, name='add_dislike'),
    url(r'^addcomment/(?P<book_id>[0-9]+)/$', views.addcomment, name='addcomment'),
    # url(r'^addcomment/(?P<book_id>[0-9]+)/$', views.addcomment, name='addcomment')
    # url(r'^sign_in/$', views.sign_in, name='sign in'),
    # url(r'^registration/$', views.registration, name='registration')

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
