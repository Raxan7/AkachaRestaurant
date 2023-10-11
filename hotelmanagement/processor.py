from .models import User_type


def user_type_list(request):
    user_type = User_type.objects.all()
    return {'user_types': user_type}
