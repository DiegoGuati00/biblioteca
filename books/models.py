from django.db import models

from core.models import User

# Create your models here.
class Autor(models.Model):
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)

class Book(models.Model):
    number = models.IntegerField(null=False)
    title = models.CharField(max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=250)
    datepublication = models.DateField()
    status = models.BooleanField(default=True)

class BookItem(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number = models.IntegerField(null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    place = models.CharField(max_length=250)
    status = models.BooleanField(default=False)