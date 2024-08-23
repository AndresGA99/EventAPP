from authApp.models import User


def get_user_role_by_user_id(user_id):
    user = User.objects.get(id=user_id)
    return user.role.name
