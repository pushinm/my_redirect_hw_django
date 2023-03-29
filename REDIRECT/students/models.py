from django.db import models
from persons.models import PersonAbstract


# Create your models here.
class Student(PersonAbstract):
    group = models.ForeignKey(
        verbose_name="Группа",
        to="Group",
        on_delete=models.CASCADE,
        related_name="student_group",
    )
    # on_class = models.ManyToManyField(
    #     verbose_name="Предмет", to="subjects.Subject", related_name="class_subject"
    # )    
    on_subject = models.ManyToManyField(
        verbose_name="Предмет", to="subjects.Subject", related_name="student_subject"
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

        ordering = ["first_name", "last_name"]


class Group(models.Model):
    name = models.CharField(
        verbose_name="Группа", max_length=100, blank=True, null=True
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"
