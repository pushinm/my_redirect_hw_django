import datetime
from django.db.models import Count, Sum, Q, F
from django.shortcuts import render, get_object_or_404
from wages.models import Wage

# Create your views here.


def get_grid_title() -> dict:
    header = {
        'teacher_title': Wage._meta.get_field('teacher').verbose_name,
        'salary_title': Wage._meta.get_field('salary').verbose_name,
        'tax_title': Wage._meta.get_field('tax').verbose_name,
        'deductions_title': Wage._meta.get_field('deductions').verbose_name,
        'alimony_title': Wage._meta.get_field('alimony').verbose_name,
        'net_title': Wage._meta.get_field('net').verbose_name,
        'go_to': 'Перейти',
        're_calculate': 'Пересчитать',
    }
    return header

   
def show_teachers_grid(request, pk=None):
    if not pk:
        template_ = 'wages_index.html'
        today_date = Q(year=datetime.date.today().year) | \
                     Q(month=datetime.date.today().month)
        q_records = Q(deductions__gt=0) & Q(pk__gte=2)
        
        teacher = Wage.objects.select_related().filter(today_date).all()
        
        annotates = Wage.objects.select_related().annotate(
                annotate_teacher=(F('teacher__first_name')),
                annotate_pk=Count('pk', filter=q_records),
                annotate_salary=Sum('salary', filter=q_records),
                annotate_deductions=Sum('deductions', filter=q_records),
                annotate_net=Sum('net', filter=q_records),
                annotate_tax_count=F('salary')/100 * F('tax'),
                annotate_alimony_count=F('salary')/100 * F('alimony'),
            ).order_by('-deductions')
        
        totals = Wage.objects.select_related().filter(today_date).\
                order_by('-deductions').\
                aggregate(Count('pk'),
                    Sum('salary'),
                    Sum('deductions'),
                    Sum('net'))

        context = {
            'header': get_grid_title(),
            'teacher': teacher,
            'totals': totals,
            'annotates': annotates
        }
        
    return render(request=request, template_name=template_, context=context)


def wage_recalculate(request, pk=None):

    template_ = 'wages_index.html'
    
    teacher = get_object_or_404(Wage, pk=pk)
    teacher.save()
    
    teacher = Wage.objects.all()
    context = {
        'header': get_grid_title(),
        'teacher': teacher,
    }
        
    return render(request=request, template_name=template_, context=context)
   
