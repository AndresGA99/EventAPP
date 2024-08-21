from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings


def request_decode_token(request):
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    return token_backend.decode(token, verify=False)
