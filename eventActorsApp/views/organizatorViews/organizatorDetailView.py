from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


from securityApp.decorators import is_granted
from authApp.models import User
from authApp.utils import request_decode_token, get_user_role_by_user_id
from eventActorsApp.models import Organizator
from eventActorsApp.serializers import OrganizatorSerializer


class OrganizatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizator.objects.all()
    serializer_class = OrganizatorSerializer
    permission_classes = (IsAuthenticated, )

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN'], settings.ROLE_NAMES['ORGANIZATOR']))
    def get(self, request, *args, **kwargs):
        token_data = request_decode_token(request)
        if get_user_role_by_user_id(token_data['user_id']) == settings.ROLE_NAMES['ORGANIZATOR']:
            organizator_user = Organizator.objects.get(id=self.kwargs['pk']).user
            if str(organizator_user.id) != token_data['user_id']:
                return Response(status=status.HTTP_403_FORBIDDEN)

        return self.retrieve(request, *args, **kwargs)

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN'], settings.ROLE_NAMES['ORGANIZATOR']))
    def patch(self, request, *args, **kwargs):
        token_data = request_decode_token(request)
        if get_user_role_by_user_id(token_data['user_id']) == settings.ROLE_NAMES['ORGANIZATOR']:
            organizator_user = Organizator.objects.get(id=self.kwargs['pk']).user
            if str(organizator_user.id) != token_data['user_id']:
                return Response(status=status.HTTP_403_FORBIDDEN)
        request.data.pop('user', None)

        return self.partial_update(request, *args, **kwargs)

    @method_decorator(is_granted(settings.ROLE_NAMES['ADMIN']))
    def delete(self, request, *args, **kwargs):
        # Delete organizator, then delete user
        organizator = Organizator.objects.get(id=self.kwargs['pk'])
        user = User.objects.get(id=organizator.user.id)
        user.delete()
        organizator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
