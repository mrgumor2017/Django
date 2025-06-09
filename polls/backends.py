from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import CustomUser

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(
                Q(username=username) | Q(email=username)
            )
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None