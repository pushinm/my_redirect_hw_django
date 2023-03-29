from django.db import models
from django.utils.translation import gettext_lazy as _
from students.models import Group


class SubjectAbstract(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=100)

    class Meta:
        abstract = True

        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("classes:class_view", kwargs={"pk": self.pk})


class Subject(SubjectAbstract):
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self) -> str:
        return f'{self.name}'


class SubjectPairChoices(models.TextChoices):
    PAIR_1 = 1, _('Первая пара')
    PAIR_2 = 2, _('Вторая пара')
    PAIR_3 = 3, _('Третья пара')
    PAIR_4 = 4, _('Четвертая пара')
    PAIR_5 = 5, _('Пятая пара')
    PAIR_6 = 6, _('Шестая пара')
    PAIR_7 = 7, _('Седьмая пара')
    PAIR_8 = 8, _('Восьмая пара')


class SubjectByDayChoices(models.TextChoices):
    MO = 1, _('Понедельник')
    TU = 2, _('Вторник')
    WE = 3, _('Среда')
    TH = 4, _('Четверг')
    FR = 5, _('Пятница')
    SA = 6, _('Суббота')
    SU = 7, _('Воскресенье')
