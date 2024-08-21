from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings

from securityApp.models import Role
from authApp.serializers import UserSerializer


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        default_role_instance = Role.objects.get(name=settings.ROLE_NAMES['ATTENDEE'])
        request.data['role'] = default_role_instance.id
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token_data = {
            'email' : request.data['email'],
            'password' : request.data['password'],    
        }
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
    