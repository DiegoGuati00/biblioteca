from tkinter import CASCADE
from turtle import update
from django.db import models
from core.models import User
from books.models import Book, BookItem
from django.db.models.signals import post_save 
from django.dispatch import receiver

# Create your models here.
class Rent(models.Model):
    
    STATES_RENT = [
        ("p", "PENDIENTE"),
        ("a", "RECLAMAR"),
        ("r", "RECLAMADO"),
        ("d", "DEVUELTO")
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(choices=STATES_RENT, max_length=1)

class Rented(models.Model):
    rent = models.ForeignKey(Rent,on_delete=models.CASCADE)
    bookItem = models.ForeignKey(BookItem,on_delete=models.CASCADE)
    dateget = models.DateTimeField(auto_now_add=True)
    dateIn = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)
    
@receiver(post_save, sender=Rented)
def update_status_rack(sender, instance, created, **kwargs):
    #after creat the book set asided it will update state the book
    if created:
        book = BookItem.objects.get(pk=instance.bookItem.id)
        book.status = True
        book.owner = User.objects.get(pk=instance.rent.owner.id)
        book.save()
    #after update the book at true it will update state set asided
    elif instance.state == True:
        rent = Rent.objects.get(pk=instance.rent.id)
        if rent.status == "a":
            rent.status = "r"
            rent.save()
    #after update the book at false it will update state set asided
    #and book will update state at False
    elif instance.state == False:
        rent = Rent.objects.get(instance.rent.id)
        if rent.status == "r":
            rent.status = "d"
            rent.save()
            book = BookItem.objects.get(pk=instance.bookItem.id)
            book.status = False
            book.save()
            