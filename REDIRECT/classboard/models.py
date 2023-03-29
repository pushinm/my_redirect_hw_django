from django.db import models

# from teachers.models import Teacher
from subjects.models import Subject, SubjectPairChoices, SubjectByDayChoices

# Create your models here.

class Classboard(models.Model):
    class_day = models.CharField(verbose_name='День недели', max_length=6, choices=SubjectByDayChoices.choices,
                                  default=SubjectByDayChoices.MO)
    class_pair = models.CharField(verbose_name='Пара', max_length=6, choices=SubjectPairChoices.choices,
                                  default=SubjectPairChoices.PAIR_1)
    subject_name = models.ForeignKey(verbose_name='Занятие', to='subjects.Subject', on_delete=models.CASCADE)
    group = models.ForeignKey(verbose_name='Группа', to='students.Group', on_delete=models.CASCADE)
    teacher = models.ManyToManyField(verbose_name='Преподаватель', to='teachers.Teacher', related_name='classboard_teacher')

    class Meta:
        ordering = ['subject_name', ]

        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self) -> str:
        return f'{self.subject_name}'
