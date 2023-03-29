from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('title', 'first_name', 'last_name', 'email', 'phone', 'image', 'testimonial',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
                                            'placeholder': 'Заголовок отзыва', 
                                            'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 
                                             'required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'label': 'Изображение'}),
            'testimonial': forms.Textarea(attrs={
                                                'class': 'form-control', 
                                                'required': 'required',
                                                'placeholder': 'Оставьте Ваш отзыв'
                                                }),
        }