from django.db import models

from applications.core.models import BaseModel

__all__ = [
    'Course',
    'Student'
]


class Course(BaseModel):
    PAZARTESI = 1
    SALI = 2
    CARSAMBA = 3
    PERSEMBE = 4
    CUMA = 5

    DAY_CHOICES = (
        (PAZARTESI, 'PAZARTESI'),
        (SALI, 'SALI'),
        (CARSAMBA, 'CARSAMBA'),
        (PERSEMBE, 'PERSEMBE'),
        (CUMA, 'CUMA'),
    )

    title = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)
    code = models.CharField(max_length=8, default=None)
    date = models.IntegerField(choices=DAY_CHOICES, default=PAZARTESI, )


    class Meta:
        ordering = ['code']

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
