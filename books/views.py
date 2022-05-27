from django.shortcuts import render
from books.permissions import IsOwnerOrReadOnlyBook
from .models import Book,BookItem,Autor
from rest_framework import viewsets,filters
from .serializer import AutorSerializer, BookItemSerializer, BookSerializer, CreateBookItemSerializer, CreateBookSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
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
    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookSerializer
        else:
            return BookSerializer
        
    def get_permissions(self):
        if self.action == ["create","update","delete"]:
            permission_classes = [IsAdminUser] 
        else:
           permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    
class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer()
    
    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookItemSerializer
        else:
            return BookItemSerializer
    # permission_classes = [IsAdminUser]
    def get_permissions(self):
        if self.action == ["create","update","delete"]:
            permission_classes = [IsAdminUser] 
        else:
           permission_classes = [IsOwnerOrReadOnlyBook]
        return [permission() for permission in permission_classes]