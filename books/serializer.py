from rest_framework import serializers
from .models import Book, BookItem,Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"       

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1
        
class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['status']
     
class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = "__all__"
class CreateBookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['status']


        
