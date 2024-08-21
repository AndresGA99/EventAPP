from rest_framework import serializers

from securityApp.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = data['name'].upper()
        return data
