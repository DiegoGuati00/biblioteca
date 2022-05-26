from django.contrib import admin
from .models import Book, Autor, BookItem
# Register your models here.

admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(BookItem)