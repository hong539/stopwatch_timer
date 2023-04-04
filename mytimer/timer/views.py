from django.shortcuts import render
import time

def timer_view(request):
    start_time = time.time()
    current_time = time.time() - start_time
    return render(request, 'timer.html', {'current_time': current_time})