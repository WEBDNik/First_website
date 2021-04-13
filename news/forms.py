from .models import Mynews
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateTimeField


class MynewsForm(ModelForm):
    class Meta:
        model = Mynews
        fields = ["title", "task", "about", "data"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание новости'
            }),
            "about": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание новости'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
       }