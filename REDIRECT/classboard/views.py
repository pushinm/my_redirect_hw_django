from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Classboard
from students.models import Group, Student
from subjects.models import SubjectByDayChoices, SubjectPairChoices


# Create your views here.


def filters_students_options(request, pk=None):
    if request.method == "POST":
        filter_q = Q(group__pk=request.POST.get("group_choice"))
        if request.POST.get("pair_choice"):
            filter_q &= Q(class_pair=request.POST.get("pair_choice"))
        if request.POST.get("day_choice"):
            filter_q &= Q(class_day=request.POST.get("day_choice"))

        return (
            Classboard.objects.filter(filter_q)
            .prefetch_related("teacher")
            .select_related("subject_name", "group")
        )

    return (
        Classboard.objects.all()
        .prefetch_related("teacher")
        .select_related("subject_name", "group")
    )


def classboard_view(request, pk=None) -> render:
    """
    Отображает пару "предмет - учитель" или, при наличии параметрах
    пути pk, конкретную пару "предмет - учитель"

    """
    if not pk:
        template_ = "classboard_all.html"

        classboard_all = filters_students_options(request)

        context = {
            "classboard_all": classboard_all,
            "group": Group.objects.all(),
            "days": SubjectByDayChoices.choices,
            "pair": SubjectPairChoices.choices,
        }
    else:
        template_ = "classboard_item.html"

        classboard_current = get_object_or_404(Classboard, pk=pk)
        students_filter_q = Q(group_id=classboard_current.group)
        students = Student.objects.filter(students_filter_q).select_related("group")

        context = {
            "classboard_current": classboard_current,
            "students": students,
        }

    return render(request=request, template_name=template_, context=context)
