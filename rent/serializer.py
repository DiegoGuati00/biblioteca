from rest_framework import serializers
from books.serializer import BookSerializer
from core.serializers import UserSerializer
from .models import Rent, Rented

class CreateRentSerializer(serializers.ModelSerializer):
    # owner=UserSerializer()
    class Meta:
        model = Rent
        fields = ["book"]















class RentSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    # owner=UserSerializer()
    class Meta:
        model = Rent
        fields = "__all__"
class ReadRentSerializer(serializers.ModelSerializer):
    owner=UserSerializer()
    # book = BookSerializer()
    class Meta:
        model = Rent
        fields = "__all__"
class UpdateRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = "__all__"
        depth = 1
class RentedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rented
        fields = "__all__"
        depth = 1