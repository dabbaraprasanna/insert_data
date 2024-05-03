from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import  Length

def insert_topic(request):
    tn=input()
    d={'QLTO':Topic.objects.all()}
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return render(request,'display_topic.html',d)

'''
def insert_webpage(request):
    tn=input('enter name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=webpage.objects.get_or_create(name=n,url=u,topic_name=TO)[0]
    WO.save()
    return HttpResponse('webpage is created successfully')'''



def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')


    #TO=Topic.objects.get_or_create(topic_name=tn)
    ''' we can use get method to get the parent table object but if parent table object is not avaia;able it throws an error'''
    LTO=Topic.objects.filter(topic_name=tn)
    d={'QLWO':webpage.objects.all()}
    if LTO:
       RTO=LTO[0]
       WO=webpage.objects.get_or_create(name=n,url=u,topic_name=RTO)[0]
       WO.save()
       return render(request,'display_webpage.html',d)
    else:
        return HttpResponse('given topic is Not  present in my parent table')

'''def insert_access(request):
    tn=input('enter topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=webpage.objects.get_or_create(name=n,url=u,topic_name=TO)[0]
    WO.save()
    d=input('enter date')
    a=input('enter a name')
    i=input('enter ipl')
    AO=AccessRecord.objects.get_or_create(date=d,author=a,ipl=i,name=WO)[0]
    AO.save()
    return HttpResponse('access created')'''

def insert_access(request):
    
    i=int(input('enter id'))
    WO=webpage.objects.get(id=i)
    d=input('enter date')
    a=input('enter author')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)
    d={'QLAO':AccessRecord.objects.all()}
    return render (request,'display_access.html',d)



def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=webpage.objects.all()
    QLWO=webpage.objects.filter(topic_name='cricket')
    QLWO=webpage.objects.all()
    QLWO=webpage.objects.exclude(topic_name='cricket')
    QLWO=webpage.objects.all().order_by('name')
    QLWO=webpage.objects.all().order_by('-name')
    QLWO=webpage.objects.filter(topic_name='cricket').order_by('name')
    QLWO=webpage.objects.all().order_by(Length('name').desc())
    QLWO=webpage.objects.all()[2::] 
    QLWO=webpage.objects.all()
    QLWO=webpage.objects.filter(name__startswith='s')
    QLWO=webpage.objects.filter(name__endswith='i')
    QLWO=webpage.objects.filter(name__contains='s')
    QLWO=webpage.objects.all()
    QLWO=webpage.objects.filter(name__in=('lakshmi','kohli'))
    QLWO=webpage.objects.filter(name__in=('sania','Sachin'))
    QLWO=webpage.objects.filter(url__endswith='in')
    QLWO=webpage.objects.filter(name__endswith='.com')


    
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date='2000-3-5')
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__year=1999)
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__month=4)
    QLAO=AccessRecord.objects.filter(date__day=4)

    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)


