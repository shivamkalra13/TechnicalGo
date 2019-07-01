from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Subject

# Create your views here.
def index(request):
    mycontext={
        'data': 'This is the first web page of the app.'
    }
    return render(request, 'first_app/index.html', context=mycontext)

def classes(request):
    GetParams = dict(request.GET)       #dictionary of GET parameters
    sub_list = []                        #If no parameter is found then this empty list will pass
    #class_list = Subject.objects.all().values('classno').distinct() #Get all distinct classno from db
    class_list = Subject.class_names
    cld = None                          #If no parameter is found then this None will pass
    sbd = None                          #If no parameter is found then this None will pass
    if(len(GetParams.keys())==1):       #Only class selected not subject
        cld = GetParams['cld'][0]          #getting classDropdown parameter
        sub_list = Subject.objects.filter(classno = cld)
    elif(len(GetParams.keys())==2):      #Both class and subject selected
        cld = GetParams['cld'][0]        #getting classDropdown parameter
        sbd = GetParams['sbd'][0]        #getting subjectDropdown parameter
        sub_list = Subject.objects.filter(classno = cld)
    mycontext={
        'sub_list':sub_list,     #List of subjects corresponding to classes
        'class_list':class_list,
        'sel_class':cld,
        'sel_sub':sbd
    }
    return render(request, 'first_app/classes.html', context=mycontext)

def navbar(request):
    return render(request, 'first_app/navbar.html')
