from django.db import models

from applications.core.models import BaseModel

__all__ = [
    'EntityType',
]


class EntityType(BaseModel):
    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255, db_index=True, )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
