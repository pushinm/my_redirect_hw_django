import datetime
from django.db import models

from django.utils.translation import gettext_lazy as _


def year_choices() -> list:
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

def month_choices() -> list:
    return [(r, r) for r in range(1, 13)]

def current_month():
    return str(datetime.date.today().month)


class Wage(models.Model):
    """Модель таблицы заработной платы учителя
    """
    teacher = models.ForeignKey(verbose_name=_('Преподаватель'),
                                    to='teachers.Teacher',
                                    on_delete=models.CASCADE,
                                    related_name='teachers_wage')
    salary = models.DecimalField(verbose_name=_('Оклад'),
                                    max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    null=True)
    tax = models.PositiveSmallIntegerField(verbose_name=_('Налог %'),
                                    blank=True,
                                    null=True,
                                    default=12)
    deductions = models.DecimalField(verbose_name=_('Вычеты'),
                                    max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    null=True,
                                    default=0)
    alimony = models.PositiveSmallIntegerField(verbose_name=_('Алименты %'),
                                    blank=True,
                                    null=True)
    net = models.DecimalField(verbose_name=_('На руки'),
                                    max_digits=10,
                                    decimal_places=2,
                                    blank=True)
    year = models.PositiveSmallIntegerField(verbose_name=_('Год'),
                                    choices=year_choices(),
                                    default=current_year())
    month = models.PositiveSmallIntegerField(verbose_name=_('Месяц'),
                                    choices=month_choices(),
                                    default=current_month())

    created_at = models.DateField(verbose_name=_('Дата создания'),
                                    auto_now_add=True)
    updated_at = models.DateField(verbose_name=_('Дата изменения'),
                                    auto_now=True)
    
    class Meta:
        verbose_name = 'Заработная плата'
        verbose_name_plural = 'Заработная плата'
        
        ordering = ['teacher', ]
        
    def __str__(self) -> str:
        return f'{self.teacher}'
    
    def save(self, *args, **kwargs):
        """
        При сохраниении происходит расчёт заработной платы послее отчислений
        и налогов (net)
        """
        if self.salary:
            tax = self.salary / 100 * self.tax if self.tax else 0
            alimony = self.salary / 100 * self.alimony if self.alimony else 0
        
            self.net = self.salary - tax - self.deductions - alimony 
        else:
            self.net = 0

        super(Wage, self).save(*args, **kwargs)
