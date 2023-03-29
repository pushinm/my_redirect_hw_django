from django.db import models
from persons.models import PersonAbstract


# Create your models here.

class Testimonial(PersonAbstract): 
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    testimonial = models.TextField(verbose_name='Отзыв')
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    active = models.BooleanField(verbose_name='Активен', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['first_name', 'last_name']

    def __str__(self)->str:
        return f'{self.title}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('', kwargs={'pk': self.pk})