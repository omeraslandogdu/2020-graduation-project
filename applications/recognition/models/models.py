from django.db import models

from applications.core.models import BaseModel

__all__ = [
    'Course',
]


class Course(BaseModel):
    title = models.CharField(max_length=255)

    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title