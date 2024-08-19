from rest_framework import serializers
from authApp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'password', 'is_active'
        ]
        
    def create(self, validated_data):
        user_instance = User.objects.create(**validated_data)
        return user_instance
    
    def to_representation(self, obj):
        return {
            'id' : obj.id,
            'email' : obj.email,
            'is_active' : obj.is_active
        }
    