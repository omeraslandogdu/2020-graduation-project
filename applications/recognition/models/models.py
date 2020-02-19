from django.db import models

from applications.core.models import BaseModel

__all__ = [
    'Course',
    'Student'
]


class Course(BaseModel):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Student(BaseModel):
    user = models.ForeignKey('User', models.DO_NOTHING)
    student_id = models.IntegerField()
    phone = models.IntegerField()
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.student_id


"""    def save(self):
        pass"""
