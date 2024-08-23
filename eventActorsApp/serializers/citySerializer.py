from rest_framework import serializers

from eventActorsApp.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id', 'name'
        ]

    def create(self, validated_data):
        city_instance = City.objects.create(**validated_data)

        return city_instance

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name
        }
