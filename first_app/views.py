from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Classes
from first_app.models import Subject

# Create your views here.
def index(request):
    mycontext={
        'data': 'This is the first web page of the app.'
    }
    return render(request, 'first_app/index.html', context=mycontext)

def classes(request):
    GetParams = dict(request.GET)       #dictionary of GET parameters
    sub_list=[]
    if(len(GetParams.keys())==1):
        cld = GetParams['cld']          #getting classDropdown parameter
        all_classes = Classes.objects.filter(classno = cld[0]).values('subcode')
        for i in all_classes:
            sub_list.append(Subject.objects.filter(subcode=i['subcode']).values('subname')[0]['subname'])
        print(sub_list)
    mycontext={
        'sub_list':sub_list
    }
    return render(request, 'first_app/classes.html', context=mycontext)

def navbar(request):
    return render(request, 'first_app/navbar.html')
