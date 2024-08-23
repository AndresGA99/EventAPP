from rest_framework import serializers

from eventActorsApp.models import Attender
from authApp.serializers import UserSerializer


class AttenderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Attender
        fields = [
            'id', 'name', 'telephone', 'user'
        ]
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = UserSerializer.create(UserSerializer(), validated_data=user_data)
        attender_instance = Attender.objects.create(user=user_instance,**validated_data)
        
        return attender_instance
    
    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'telephone': obj.telephone,
            'user': UserSerializer.to_representation(UserSerializer(), obj.user)
        }
