from rest_framework import serializers

from eventActorsApp.models import Attender, City
from .citySerializer import CitySerializer
from authApp.serializers import UserSerializer


class AttenderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    city = CitySerializer()

    class Meta:
        model = Attender
        fields = [
            'id', 'name', 'telephone', 'city', 'user'
        ]
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        city_data = validated_data.pop('city')
        user_instance = UserSerializer.create(UserSerializer(), validated_data=user_data)
        city_instance = CitySerializer.create(CitySerializer(), validated_data=city_data)
        attender_instance = Attender.objects.create(user=user_instance, city=city_instance, **validated_data)
        
        return attender_instance
    
    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'telephone': obj.telephone,
            'user': UserSerializer.to_representation(UserSerializer(), obj.user),
            'city': CitySerializer.to_representation(CitySerializer(), obj.city)
        }
