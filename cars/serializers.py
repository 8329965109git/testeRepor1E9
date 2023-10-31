from rest_framework import serializers
from .models import car, Maker


class Makerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = "__all__"
