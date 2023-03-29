from django.db import models
from persons.models import PersonAbstract


# Create your models here.

class ContactPage(models.Model):
    description = models.CharField(verbose_name='Описание', max_length=250, blank=True)
    office = models.CharField(verbose_name='Офис', max_length=150, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=50, blank=True)
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self) -> str:
        return f'{self.description}'


class ContactPageForm(PersonAbstract):
    subject = models.CharField(verbose_name='Тема', max_length=100)
    message = models.TextField(verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        return f'{self.subject}'
