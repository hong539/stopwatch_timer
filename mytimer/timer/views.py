from django.shortcuts import render

def stopwatch(request):
    return render(request, 'stopwatch.html', {})