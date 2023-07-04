from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.db.models.functions import *
# Create your views here.
from django.http import HttpResponse



def topic_form(request):
    if request.method == 'POST':
        topic_name=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
        TO.save()
        return HttpResponse('data is inserted')
    return render(request,'topic.html')  

def Webpage_form(request):
    if request.method == 'POST':
        topic_name=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
        TO.save()
        name=input('enter name')
        url=input('enter url')
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('Webpage data created')
    return render(request,'webpage.html')


def AccessRecord_form(request):
    if request.method == 'POST':
        topic_name=request.POST['tn']
        TO=Topic.objects.get(topic_name=topic_name)
        TO.save()
        name=input('enter name')
        url=input('enter url')
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name)
        WO.save()
        date=input('enter date')
        author=input('enter author')
        ARO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        ARO.save()
    return render(request,'AccessRecord.html')