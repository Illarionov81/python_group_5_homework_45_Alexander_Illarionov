from django import forms
from .models import STATUS_CHOICES

defaul_status = STATUS_CHOICES[0][0]


class TaskForm(forms.Form):
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, initial=defaul_status, label='Статаус задачи: ')
    summary = forms.CharField(max_length=300, required=True, label='Задание')
    description = forms.CharField(max_length=3500, required=False, initial="None description",
                                  label='Описание', widget=forms.Textarea)
    completion_time = forms.DateField(required=False, initial=None, label='Время выполнения',
                                      widget=forms.DateInput(attrs={'type': 'date'}))
