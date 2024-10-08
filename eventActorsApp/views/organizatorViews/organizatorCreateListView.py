from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from eventActorsApp.models import Organizator
from securityApp.models import Role
from eventActorsApp.serializers import OrganizatorSerializer
from decorators.security import is_granted
from utils.paginators import DefaultPaginator


class OrganizatorCreateListView(generics.ListCreateAPIView):
    queryset = Organizator.objects.all()
    serializer_class = OrganizatorSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = DefaultPaginator

    def get_serializer_context(self):
        context = super().get_serializer_context()
        self.request.resolver_match.url_name = 'organizator-list'
        context['request'] = self.request
        return context

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN']))
    def post(self, request, *args, **kwargs):
        default_role_instance = Role.objects.get(name=settings.ROLE_NAMES['ORGANIZATOR'])
        request.data['user']['role'] = default_role_instance.id

        return self.create(request, *args, **kwargs)
