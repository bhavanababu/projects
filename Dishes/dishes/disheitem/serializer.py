from rest_framework import serializers
from disheitem.models import Dishes
class Dishserializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()


class Dishemodelserializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"
