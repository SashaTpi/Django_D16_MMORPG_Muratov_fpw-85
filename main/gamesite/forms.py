from django.forms import ModelForm, TextInput, EmailInput
from .models import Note, Response


class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['user']
        widgets = {'title': TextInput(attrs={'size': 98, 'placeholder': 'Название объявления'})}


class ResponseForm(ModelForm):

    class Meta:
        model = Response
        fields = ['content', ]
        widgets = {'content': TextInput(attrs={'size': 50, 'placeholder': 'Введите свои контакты'})}