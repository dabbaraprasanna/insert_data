from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input()
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is created successfully')

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
    if LTO:
       RTO=LTO[0]
       WO=webpage.objects.get_or_create(name=n,url=u,topic_name=RTO)[0]
       WO.save()
       return HttpResponse('webpage is created successfully')
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
    
    n=input('enter name')
    d=input('enter date')
    a=input('enter author')
    i=input('enter ipl')

    LTO=webpage.objects.filter(name=n)
    if LTO:
        RTO=LTO[0]
        AO=AccessRecord.objects.get_or_create(date=d,author=a,ipl=i,name=WO)[0]
        AO.save()
        return HttpResponse('access created')
    else:
        return HttpResponse('given topic is not present')



def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)
