import binascii
import os

from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from applications.core.models import BaseModel


__all__ = [
    'UserToken',
    'User',
    'UserType',
]

class ClientManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class UserToken(Token):
    class Meta(Token.Meta):
        db_table = 'client_token'
        abstract = False



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that is built in.


    objects = ClientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class UserType(BaseModel):
    title = models.CharField(max_length=255, help_text='Title of user type for related entity_type.')
    entity_type = models.ForeignKey('EntityType', models.DO_NOTHING, related_name='user_type',
                                    help_text='Entity type id for user type.')
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title





