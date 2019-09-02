from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, admin=False, staff=False, active=True):
        if not email:
            raise ValueError("User must have an email address")
            if not password:
                raise ValueError("User must have a password")
        user_obj = self.model(
            email = self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.staff = staff
        user_obj.admin = admin
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff_user(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            staff=True,
            admin=True
        )
        return user
