from django.db import models

from applications.core.models import BaseModel

__all__ = [
    'EntityType',
]


class EntityType(BaseModel):
    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255, db_index=True, )
    client = models.ForeignKey('Client', models.DO_NOTHING)

    class Meta:
        unique_together = ['client', 'key']
        ordering = ['title']

    def __str__(self):
        return self.title
