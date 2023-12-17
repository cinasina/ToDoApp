from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Creates and saves a User with the given email, password.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    """
    Creates and saves a superuser with the given email, password.
    """

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.save(using=self._db)
        return user
