from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .managers import (
    TrashedManager,
    SoftDeletableManager,
)

__all__ = [
    'DeletableMixin',
    'BaseModel',
    'BaseTimestampModel',
]


class DeletableMixin(models.Model):
    deleted_at = models.DateTimeField(editable=False, blank=True, null=True)

    objects = SoftDeletableManager()
    trash = TrashedManager()

    def delete(self, *args, **kwargs):
        # keyword argument trash has default value True
        trash = kwargs.get('trash', True)
        if not self.deleted_at and trash:
            self.deleted_at = timezone.now()
            self.status = BaseModel.STATUS_DELETED
            self.save()
        elif trash is False:
            # hard delete
            super(DeletableMixin, self).delete()

    def restore(self, commit=True):
        self.deleted_at = None
        if commit:
            self.save()

    class Meta:
        abstract = True


class BaseTimestampModel(DeletableMixin):
    """
    Base timestamp model
    """
    id = models.AutoField(name='id', primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True, null=True)

    class Meta:
        abstract = True


class BaseModel(BaseTimestampModel):
    """
    Use this model for common functionality
    """

    STATUS_ACTIVE = 1
    STATUS_PASSIVE = 0
    STATUS_DELETED = -1
    STATUS_DEFAULT = 1
    STATUS_WAITING = 2

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_PASSIVE, 'Passive'),
        (STATUS_DELETED, 'Deleted'),
        (STATUS_WAITING, 'Waiting'),

    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DEFAULT, )

    class Meta:
        abstract = True

    @staticmethod
    def status_to_json():
        status_json = []
        for id, value in BaseModel.STATUS_CHOICES:
            status_json.append({
                'id': id,
                'value': value
            })
        return status_json
