import binascii
import os

from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from applications.core.models import BaseModel


__all__ = [
    'Client',
    'ClientToken',
    'User',
    'UserType',
]


class Client(AbstractUser):
    app_name = models.CharField(max_length=155)
    app_id = models.CharField(max_length=55, blank=True)

    class Meta(AbstractUser.Meta):
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def save(self, *args, **kwargs):
        if not self.app_id:
            self.app_id = self.generate_app_id()
        if not self.app_name:
            self.app_name = self.username
        self.set_password(raw_password=self.password)
        return super(Client, self).save(*args, **kwargs)

    def generate_app_id(self):
        return binascii.hexlify(os.urandom(3)).decode()

    def __str__(self):
        return self.app_name


class ClientToken(Token):
    class Meta(Token.Meta):
        db_table = 'client_token'
        abstract = False


class User(BaseModel):
    fullname = models.CharField(max_length=255, blank=True, null=True, help_text='Fullname of user.')
    email = models.CharField(max_length=255, help_text='Email of user.')
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        unique_together = ('email', 'client')
        ordering = ['id']

    def __str__(self):
        return self.fullname


class UserType(BaseModel):
    title = models.CharField(max_length=255, help_text='Title of user type for related entity_type.')
    entity_type = models.ForeignKey('EntityType', models.DO_NOTHING, related_name='user_type',
                                    help_text='Entity type id for user type.')
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title





