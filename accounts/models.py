from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    first_name = models.CharField(max_length=128, verbose_name='نام')
    last_name = models.CharField(max_length=128, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه')
    national_id = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')

    is_editor = models.BooleanField(
        default=False,
        help_text="Designates whether the user is an editor.",
        verbose_name='ویرایشگر'
    )
    is_journalist = models.BooleanField(
        default=False,
        help_text="Designates whether the user is a journalist.",
        verbose_name='بررسی کننده'
    )

    is_active = models.BooleanField(
        default=True,
        help_text=
        """Designates whether this user should be treated as active. 
        Unselect this instead of deleting accounts.""",
        verbose_name='فعال'
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
        verbose_name='ادمین'
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text=
        """Designates that this user has all permissions without 
        explicitly assigning them.""",
        verbose_name='فوق ادمین'
    )

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "national_id", "email"]

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.get_full_name()
