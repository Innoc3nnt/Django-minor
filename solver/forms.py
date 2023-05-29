from django.forms import ModelForm, Select
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'num']
        choices = (('Какое это число: положительное, отрицательное, ноль?',
                     'Дано вещественное число. Определить, какое это число: положительное, отрицательное, ноль.'), 
                   ('Вычислить х = a**2 + 4a + 5  при а < 62; в противном случае x = 1/(a**2) + 4a + 5)',
                    "Дано вещественное число A. Вычислить х = a**2+4+5  при а < 62; в противном случае x = 1/(x**2) + 4x + 5)"))
        widgets = {
            'task' : Select(choices=choices)
        }