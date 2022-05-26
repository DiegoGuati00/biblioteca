from django.shortcuts import render
from .models import Book,BookItem,Autor
from rest_framework import viewsets,filters
from .serializer import AutorSerializer, BookItemSerializer, BookSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAdminUser]
    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['title', 'autor','categoria','datepublication']
    search_fields = ['title', 'autor','categoria','datepublication']
    # permission_classes = [IsAdminUser]
    
class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [IsAdminUser]