from rest_framework import generics
from django.utils.decorators import method_decorator
from django.conf import settings
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from eventActorsApp.models import Attender
from securityApp.models import Role
from eventActorsApp.serializers import AttenderSerializer 
from decorators.security import is_granted
from utils.paginators import DefaultPaginator

class AttenderCreateListView(generics.ListCreateAPIView):
    queryset = Attender.objects.all()
    serializer_class = AttenderSerializer
    pagination_class = DefaultPaginator

    @permission_classes([IsAuthenticated ])
    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN'],settings.ROLE_NAMES['ORGANIZATOR']))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        default_role_instance = Role.objects.get(name=settings.ROLE_NAMES['ATTENDEE'])
        request.data['user']['role'] = default_role_instance.id
        return self.create(request, *args, **kwargs)
