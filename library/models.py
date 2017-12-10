# -*- coding: utf-8 -*-
from django.db import models

SHORT_DESCRIPTION_LEN = 120

# class Genre(models.Model):
#     class Meta():
#         db_table = "book"
#    genre = models.CharField(max_length=100)


class Book(models.Model):
    class Meta():
        db_table = "book"
    book_title = models.CharField(max_length=100)
    book_image = models.ImageField(null=True, blank=True, upload_to="images/", help_text='150x150px', verbose_name='Image')
    book_author = models.CharField(max_length=50)
    book_year = models.CharField(max_length=4)
    book_genre = models.CharField(max_length=50)
    book_description = models.TextField()
    book_text = models.FileField(upload_to="text/", default="")
    book_rating = models.IntegerField(default=0)
    book_likes = models.IntegerField(default=0, verbose_name='Likes')



    def __str__(self):
        return self.book_title

    def get_short_description(self):
        if len(self.book_description) > SHORT_DESCRIPTION_LEN:
            return self.book_description[:SHORT_DESCRIPTION_LEN]
        else:
            return self.book_description

    def bit(self):
        if self.book_image:
            return u'<img src="%s" width="70"/>' % self.book_image.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True




class Comments(models.Model):
    class Meta():
        db_table = "comments"
    comments_text = models.TextField()
    comments_book = models.ForeignKey(Book)
    comments_date = models.DateTimeField()
