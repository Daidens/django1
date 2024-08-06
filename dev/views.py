from django.http import HttpResponse
from django.shortcuts import render


def runoob(request):
    context          = {}
    context['hello'] = 'Hello Dragon'
    return render(request, 'index.html', context)
 
def hello(request):
    return render(request, 'home.html')