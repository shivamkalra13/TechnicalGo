from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    mycontext={
        'data': 'This is the first web page of the app.'
    }
    return render(request, 'first_app/index.html', context=mycontext)

def classes(request):
    return render(request, 'first_app/classes.html')

def navbar(request):
    return render(request, 'first_app/navbar.html')
