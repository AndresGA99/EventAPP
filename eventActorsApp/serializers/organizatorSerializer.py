from rest_framework import serializers

from eventActorsApp.models import Organizator
from authApp.serializers import UserSerializer


class OrganizatorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Organizator
        fields = [
            'id', 'nit', 'name', 'telephone', 'contact_email', 'user'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = UserSerializer.create(UserSerializer(), validated_data=user_data)

        organizator_instance = Organizator.objects.create(user=user_instance, **validated_data)

        return organizator_instance

    def to_representation(self, obj):
        request = self.context.get('request')
        representation = {
            'id': obj.id,
            'nit': obj.nit,
            'name': obj.name,
            'telephone': obj.telephone,
            'contact_email': obj.contact_email,
            'user': UserSerializer.to_representation(UserSerializer(), obj.user)
        }

        if request and request.method == 'GET' and request.resolver_match.url_name == 'organizator-list':
            representation.pop('user', None)

        return representation
    