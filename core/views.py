from django.shortcuts import render
from .models import User
from rent.models import Rent
from books.models import BookItem
from rent.serializer import RentSerializer
from books.serializer import BookItemSerializer
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
    
    