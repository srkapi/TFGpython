from django.http import HttpResponse
from django.core import serializers
from models import Post,Measure
from datetime import date
from django.shortcuts import render
from pymongo import MongoClient

def index(request):
    connection = MongoClient()
    db = connection['project']
    collection = db.app_measure
    data = collection.find()
    context = {'data': data}
    connection.close()
    return render(request, 'index.html', context)



def measure(request):
    sensor=request.GET['sensor']
    measure=request.GET['measure']
    post = Measure.objects.create( sensor=sensor, type=2,value=measure,fecha=date.today())
    post.save()
    return HttpResponse("medida insertada con exist")# Create your views here.
