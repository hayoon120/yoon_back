from django.shortcuts import render
import os
import psutil
from .models import Count
import datetime

# Create your views here.

def helloworld(request):
    category = request.GET.get('message', None)
    context = {
        'message' : category
    } 
    date = Count.objects.create()
    return render(request, 'helloworld.html', context)

def status(request):
    pid = os.getpid()
    py = psutil.Process(pid)

    # cpu_usage   = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
    # cpu_usage   = cpu_usage.replace("\n","")
    cpu_usage = psutil.cpu_percent()

    memory_usage  = round(py.memory_info()[0] /2.**30, 2)

    current = datetime.datetime.now()

    one_second_ago = current - datetime.timedelta(seconds=1)
    one_minute_ago = current - datetime.timedelta(minutes=1)
    ten_minutes_ago = current - datetime.timedelta(minutes=10)

    one_second = Count.objects.filter(date__range=[one_second_ago, current]).count()
    one_minute = Count.objects.filter(date__range=[one_minute_ago, current]).count()
    ten_minutes = Count.objects.filter(date__range=[ten_minutes_ago, current]).count()


    context = {
        'cpu_usage' : cpu_usage,
        'mem_usage' : memory_usage,
        'one_second' : one_second,
        'one_minute' : one_minute,
        'ten_minutes' : ten_minutes
    }

    return render(request, 'status.html', context)