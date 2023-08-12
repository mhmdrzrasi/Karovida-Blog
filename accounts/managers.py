from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, national_id, email, password=None):
        """
        Creates and saves a User with the given first_name, last_name,
        phone_number, national_id, email and password.
        """
        if not first_name:
            raise ValueError("Users must have a first name")

        if not last_name:
            raise ValueError("Users must have a last name")

        if not phone_number:
            raise ValueError("Users must have a phone number")

        if not national_id:
            raise ValueError("Users must have a national_id")

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            national_id=national_id,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, national_id, email, password=None):
        """
        Creates and saves a superuser with the given first_name, last_name,
        phone_number, national_id, email and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            phone_number,
            national_id,
            email,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
