from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.conf import settings

from securityApp.models import Role
from securityApp.serializers import RoleSerializer
from securityApp.decorators import is_granted


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated, )

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN']))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
