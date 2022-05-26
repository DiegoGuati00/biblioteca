from rest_framework import serializers
from .models import Book, BookItem,Autor

class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = "__all__"
        # depth = 1

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
        # depth = 1
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1