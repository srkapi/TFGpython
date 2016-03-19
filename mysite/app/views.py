from django.http import HttpResponse
from django.core import serializers
from models import Post,Measure
from flask  import Flask, jsonify
from datetime import datetime
from django.shortcuts import render
from pymongo import MongoClient
def index(request):
    return render(request, 'index.html')



def measureAdd(request):
    sensor=request.GET['sensor']
    measure=request.GET['measure']
    post = Measure.objects.create(sensor=sensor, type=2, value=measure, fecha=datetime.now())
    post.save()
    return HttpResponse("medida insertada con exist")# Create your views here.


def measure(request):
    connection = MongoClient()
    db = connection['project']
    collection = db.app_measure
    data = collection.find()
    length = collection.count()
    context = {'data':  data ,'count': length}
    connection.close()
    return render(request, 'measure.html',context)
