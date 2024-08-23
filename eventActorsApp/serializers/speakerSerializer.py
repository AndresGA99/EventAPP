from rest_framework import serializers

from eventActorsApp.models import Speaker, Organizator
from authApp.models import User
from authApp.serializers.userSerializer import UserSerializer


class SpeakerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Speaker
        fields = ['id', 'name', 'surname', 'description', 'organization', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        organization_id = validated_data.pop('organization')
        user = User.objects.create(**user_data)
        organization = Organizator.objects.get(id=organization_id.id)
        speaker = Speaker.objects.create(user=user, organization=organization, **validated_data)
        return speaker

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation
