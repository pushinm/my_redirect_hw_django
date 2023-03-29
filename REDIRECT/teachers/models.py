from django.db import models

from persons.models import PersonAbstract


class Teacher(PersonAbstract):
    subject = models.ManyToManyField(to='subjects.Subject', related_name='subject_teacher')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('teachers:view_teacher', kwargs={'pk': self.pk})
