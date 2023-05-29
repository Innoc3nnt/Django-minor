from django.shortcuts import render
from .forms import TaskForm
from .models import Task
from django.db.models import Count, Avg, Min, Max, StdDev, Sum


def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Form Error!")
    form = TaskForm
    table = Task.objects.values_list()
    result = []
    for row in table:
        print(row)
        if row[1] == 'Какое это число: положительное, отрицательное, ноль?':
            if row[2] < 0:
                result.append('Отрицательное')
            elif row[2] == 0:
                result.append('Ноль')
            else:
                result.append('Положительное')
        elif row[1] == "Вычислить х = a**2 + 4a + 5  при а < 62; в противном случае x = 1/(a**2) + 4a + 5)":
            if row[2] < 62:
                result.append(row[2] ** 2 + 4 * row[2] + 5)
            else:
                result.append(1 / (row[2] ** 2) + 4 * row[2] + 5)
        else:
            result.append('')
    context = {
        "form": form,
        "table":table,
        "result":result
        }
    print(result)
    return render(request, "index.html", context)


def table(request):
    col_names = [i.verbose_name for i in Task._meta.get_fields()]
    table = Task.objects.values_list()
    data = Task.objects.all()
    stats = [
        data.aggregate(Count("num")),
        data.aggregate(Avg("num")),
        data.aggregate(Min("num")),
        data.aggregate(Max("num")),
        data.aggregate(StdDev("num")),
        data.aggregate(Sum("num")),
    ]
    context = {"col_names": col_names, "table": table, "stats": stats}
    return render(request, "table.html", context)
