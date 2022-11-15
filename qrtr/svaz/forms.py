from .models import *
from django.forms import ModelForm, TextInput, Textarea


class SvazForm(ModelForm):
    class Meta:
        model = Svaz
        fields = ['last_name', 'first_name', 'sposob', 'pravki',]
        widgets = {
            'last_name': TextInput(attrs={
                'placeholder': 'Фамилия',
                'class': 'contact-form-lastname'
            }),
            'first_name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'contact-form-name'
            }),
            'sposob': TextInput(attrs={
                'placeholder': 'Способ обратной связи',
                'class': 'contact-form-type'
            }),
            'pravki': Textarea(attrs={
                'placeholder': 'Внесите правки/Опишите проблему',
                'class': 'contact-form-changes'
            }),
        }