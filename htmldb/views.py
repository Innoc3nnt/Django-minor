from django.shortcuts import render, redirect
from .models import Pages

def index(request):
    return redirect('page/1')

def page(request, pk):
    # content = Pages.objects.get(id = pk).cotntent
    content = getattr(Pages.objects.get(id = pk), 'content')
    context = {
        'content' : content
    }
    return render(request, 'page.html', context)
