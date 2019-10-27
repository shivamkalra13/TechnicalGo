from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Subject
from first_app.models import Notes
from first_app.models import Videos
from first_app.models import Books

#Some Auxiliary functions
def getNotes(sub,cls):
    notesLst = list()
    if(sub and cls):
        subcode_selected = (Subject.objects.filter(classno = cls).filter(subname = sub))[0].subcode
        notesLst = Notes.objects.filter(subcode = subcode_selected)
    elif(cls):
        queryset = Subject.objects.filter(classno = cls)
        for obj in queryset:
            notesLst.extend(list(Notes.objects.filter(subcode = obj.subcode)))
    else:
        notesLst = Notes.objects.all()
    return notesLst

def getBooks(sub,cls):
    booksLst = list()
    if(sub and cls):
        subcode_selected = (Subject.objects.filter(classno = cls).filter(subname = sub))[0].subcode
        booksLst = Books.objects.filter(subcode = subcode_selected)
    elif(cls):
        queryset = Subject.objects.filter(classno = cls)
        for obj in queryset:
            booksLst.extend(list(Books.objects.filter(subcode = obj.subcode)))
    else:
        booksLst = Books.objects.all()
    return booksLst

def getVideos(sub,cls):
    videosLst = list()
    if(sub and cls):
        subcode_selected = (Subject.objects.filter(classno = cls).filter(subname = sub))[0].subcode
        videosLst = Videos.objects.filter(subcode = subcode_selected)
    elif(cls):
        queryset = Subject.objects.filter(classno = cls)
        for obj in queryset:
            videosLst.extend(list(Videos.objects.filter(subcode = obj.subcode)))
    else:
        videosLst = Videos.objects.all()
    return videosLst

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
    class_list = Subject.class_names    #list of all the class names in Subject model
    cld = None                          #If no parameter is found then this None will pass(selected class)
    sbd = None                          #If no parameter is found then this None will pass(selected subject)
    if(len(GetParams.keys())==1):       #Only class selected not subject
        cld = GetParams['cld'][0]          #getting classDropdown parameter
        sub_list = Subject.objects.filter(classno = cld)
    elif(len(GetParams.keys())==2):      #Both class and subject selected
        cld = GetParams['cld'][0]        #getting classDropdown parameter
        sbd = GetParams['sbd'][0]        #getting subjectDropdown parameter
        sub_list = Subject.objects.filter(classno = cld)

    #getting the notes objects list according to the selected suject and class.
    notes_lst = getNotes(sbd,cld)
    books_lst = getBooks(sbd,cld)
    videos_lst = getVideos(sbd,cld)

    mycontext={
        'sub_list':sub_list,     #List of subjects corresponding to classes
        'class_list':class_list,
        'sel_class':cld,
        'sel_sub':sbd,
        'notes_list':notes_lst,
        'books_list':books_lst,
        'videos_list':videos_lst
    }
    return render(request, 'first_app/classes.html', context=mycontext)

def navbar(request):
    return render(request, 'first_app/navbar.html')
