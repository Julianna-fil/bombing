from django.shortcuts import render
from django.http import HttpResponse

#from models import News
from .models import Info


def index(request):
    info = Info.objects.all()  # .order_by('-importance')
    return render(request, 'index.html', {'info': info})


def information(request):
    info = Info.objects.all()  # .order_by('-importance')
    return render(request, 'information.html', {'info': info})
