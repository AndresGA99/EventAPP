from rest_framework import generics
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from eventActorsApp.models import Speaker, Organizator
from securityApp.models import Role
from eventActorsApp.serializers import SpeakerSerializer
from decorators.security import is_granted
from utils.authUtils import request_decode_token
from utils.paginators import DefaultPaginator


class SpeakerCreateListView(generics.ListCreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = DefaultPaginator


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_decorator(is_granted(settings.ROLE_NAMES['ORGANIZATOR']))
    def post(self, request, *args, **kwargs):
        token_data = request_decode_token(request)
        organization_id = Organizator.objects.get(user_id=token_data['user_id'])
        default_role_instance = Role.objects.get(name=settings.ROLE_NAMES['SPEAKER'])
        request.data['user']['role'] = default_role_instance.id
        request.data['organization'] = organization_id.id

        return self.create(request, *args, **kwargs)
