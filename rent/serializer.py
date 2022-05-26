from rest_framework import serializers
from core.serializers import UserSerializer
from .models import Rent, Rented

class RentSerializer(serializers.ModelSerializer):
    # owner=UserSerializer()
    class Meta:
        model = Rent
        fields = "__all__"
class ReadRentSerializer(serializers.ModelSerializer):
    owner=UserSerializer()
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