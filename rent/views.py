from ast import Delete
from venv import create
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from books.models import Book, BookItem
from books.serializer import BookItemSerializer
from rent.models import Rent, Rented
from rent.serializer import RentSerializer,ReadRentSerializer, RentedSerializer, UpdateRentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.
class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    
    def get_serializer_class(self, *args, **kwargs):
        if self.action == "create":
            return RentSerializer
        # elif self.action == "update":
        #     return UpdateRentSerializer
        else:
            return ReadRentSerializer
        
    # def get_permissions(self):
    #     if self.action == "books_rented"or"create":
    #         permission_classes = [IsAuthenticated] 
    #     # elif self.action == "create":
    #     #     permission_classes = [IsAuthenticated] 
    #     else:
    #        permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        #get the book that user want
            bookExist = BookItem.objects.filter(
                book = request.data["Book"],
                status = False
            ).values_list("id",flat=True)
            #validate if exist a copy and create request this user
            if len(bookExist):
                thisBookExist = Rent.objects.create(
                    owner = self.request.user,
                    book = get_object_or_404(Book,pk=request.data["Book"]),
                    status = "a"
                )
                reclaim = Rented.objects.create(
                    rent = thisBookExist,
                    bookItem = get_object_or_404(BookItem,pk=bookExist[0])
                )
                serializer= RentedSerializer(reclaim)
                return Response(serializer.data)
            #this not exist
            else:
                thisBookExist = Rent.objects.create(
                    owner = self.request.user,
                    book = get_object_or_404(Book,pk=request.data["Book"]),
                    status = "p"
                )
            serializer= RentSerializer(thisBookExist)
            return Response(serializer.data)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        # # get number books rented
        
        
        # limitRent = Rent.objects.filter(
        #     status = "r",
        #     owner__email = self.request.user
        # )
        # # validate max books and create
        # if len(limitRent.values_list("BookItem",flat=True)) < 5:
        #     limitRent = Rent.objects.create(
        #         owner = self.request.user,
        #         BookItem = get_object_or_404(BookItem,pk=request.data["BookItem"],status = False)
        #     )
        #     serializer= RentSerializer(limitRent)
        #     return Response(serializer.data)
        # #limit exceeded
        # return Response(data="limite superado",status=status.HTTP_423_LOCKED)
    
    #books rented for a user
    # @action(detail=False)
    # def books_rented(elf, request,  pk=None):
    #     renteds = Rent.objects.filter(
    #         owner__email = request.user
    #     ).values_list("BookItem", flat=True)
    #     booksRent= BookItem.objects.filter(
    #         id__in = renteds,
    #         status = True
    #     )
    #     if booksRent:
    #         serializer = BookItemSerializer(booksRent, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_404_NOT_FOUND)