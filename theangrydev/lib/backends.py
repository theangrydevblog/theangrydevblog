from django.contrib.auth.backends import BaseBackend
from theangrydev.models import User

class AngryDevAuth(BaseBackend):
    def get_user(self, user_id):
        user = User.objects.filter(pk=user_id).first()
        return user
