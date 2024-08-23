from functools import wraps
from django.core.exceptions import PermissionDenied

from utils import request_decode_token
from authApp.models import User


def is_granted(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            token_data = request_decode_token(request)
            user = User.objects.get(id=token_data['user_id'])
            user_role = user.role
            if user_role.name in roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied('No tienes permisos para acceder a este recurso')
        return _wrapped_view
    return decorator
