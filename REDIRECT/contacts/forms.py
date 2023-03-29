from django import forms
from .models import ContactPageForm


# class ContactForm(forms.Form):
#     first_name = forms.CharField(label='Имя', help_text='Имя', max_length=150, required=True)
#     last_name = forms.CharField(label='Фамилия', help_text='Фамилия', max_length=150,
#                                 required=True)
#     email = forms.EmailField(label='e-mail', help_text='e-mail', required=True)
#     phone = forms.CharField(label='Телефон', help_text='Телефон', max_length=14, required=True)
#     subject = forms.CharField(label='Тема', help_text='Тема', max_length=100, required=True)
#     message = forms.CharField(label='Текст сообщения', help_text='Текст сообщения', widget=forms.Textarea)
#

class ContactFormDB(forms.ModelForm):
    class Meta:
        model = ContactPageForm
        fields = ('subject', 'first_name', 'last_name', 'phone', 'email', 'message')

        widgets = {
            'subject': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Предмет сообщения'
            }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Фамилия'
            }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Телефон'
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Сообщение'
            }),
        }
