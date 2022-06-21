from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello')

def say_congrats(request):
    return render(request, 'congrats.html', {
        'name': 'Fajar Hamdani',
        'adult': True
    })