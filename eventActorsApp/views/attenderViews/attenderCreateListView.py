from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from eventActorsApp.models import Attender
from securityApp.models import Role
from eventActorsApp.serializers import AttenderSerializer 
from securityApp.decorators import is_granted


class AttenderListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class AttenderCreateListView(generics.ListCreateAPIView):
    queryset = Attender.objects.all()
    serializer_class = AttenderSerializer
    pagination_class = AttenderListPagination
    
   # @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN'],settings.ROLE_NAMES['ORGANIZATOR']))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        default_role_instance = Role.objects.get(name=settings.ROLE_NAMES['ATTENDEE'])
        request.data['user']['role'] = default_role_instance.id
        return self.create(request, *args, **kwargs)
