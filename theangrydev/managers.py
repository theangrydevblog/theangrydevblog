from django.contrib.auth.models import BaseUserManager
from uuid import uuid4

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, avatar=None, uuid=None):
        if not email:
            raise ValueError("User must have an email address")
            if not password:
                raise ValueError("User must have a password")
        uuid_for_user = uuid4()
        user_obj = self.model(
            email = self.normalize_email(email),
            uuid = uuid_for_user
        )

        user_obj.avatar = f"https://api.adorable.io/avatars/40/{uuid_for_user}.png"
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staff_user(self, email, password=None):
        uuid_for_user = uuid4()
        user = self.create_user(
            email=email,
            password=password,
            uuid=uuid_for_user,
            avatar = f"https://api.adorable.io/avatars/40/{uuid_for_user}.png"
        )
        return user

    def create_superuser(self, email, password=None):
        uuid_for_user = uuid4()
        user = self.create_user(
            email=email,
            uuid=uuid_for_user,
            avatar = f"https://api.adorable.io/avatars/40/{uuid_for_user}.png",
            password=password
        )
        return user
