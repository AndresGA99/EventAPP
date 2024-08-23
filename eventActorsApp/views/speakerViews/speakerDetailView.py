from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


from decorators.security import is_granted
from authApp.models import User
from utils.authUtils import request_decode_token, get_user_role_by_user_id
from eventActorsApp.models import Speaker
from eventActorsApp.serializers import SpeakerSerializer


class SpeakerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN'], settings.ROLE_NAMES['ORGANIZATOR'], settings.ROLE_NAMES['SPEAKER']))
    def patch(self, request, *args, **kwargs):
        token_data = request_decode_token(request)
        if get_user_role_by_user_id(token_data['user_id']) == settings.ROLE_NAMES['SPEAKER']:
            speaker_user = Speaker.objects.get(id=self.kwargs['pk']).user
            if str(speaker_user.id) != token_data['user_id']:
                return Response(status=status.HTTP_403_FORBIDDEN)
        request.data.pop('user', None)

        return self.partial_update(request, *args, **kwargs)

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN'], settings.ROLE_NAMES['ORGANIZATOR']))
    def delete(self, request, *args, **kwargs):
        speaker = Speaker.objects.get(id=self.kwargs['pk'])
        user = User.objects.get(id=speaker.user.id)
        user.delete()
        speaker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
