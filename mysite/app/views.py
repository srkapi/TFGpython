from django.http import *
from django.core import serializers
from models import Post,Measure , Users
from flask  import Flask, jsonify
from datetime import datetime
from django.shortcuts import *
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from form import UserForm
import logging
logger = logging.getLogger(__name__)

@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')



def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/app/')
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return render_to_response('login.html', context_instance=RequestContext(request))




def measureAdd(request):
    sensor=request.GET['sensor']
    measure=request.GET['measure']
    post = Measure.objects.create(sensor=sensor, type=2, value=measure, fecha=datetime.now())
    post.save()
    return HttpResponse("medida insertada con exist")# Create your views here.

@login_required(login_url='login/')
def measure(request):
    connection = MongoClient()
    db = connection['project']
    collection = db.app_measure
    data = collection.find()
    length = collection.count()
    context = {'data':  data ,'count': length}
    connection.close()
    return render(request, 'measure.html',context)

@login_required(login_url='login/')
def list_user(request):
    list=User.objects.all()
    context = {'data': list}
    return render(request, 'user.html',context)


@login_required(login_url='login/')
def user_new(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        userPass = request.POST.get('pass')
        userMail = request.POST.get('email')
        name = request.POST.get('cname')
        lastName = request.POST.get('lastName')
        admin = request.POST.get('admin')
        if admin == '1':
            adminNumber = True
        else:
            adminNumber = False
        user = Users.objects.create(name=name, last_name=lastName, user=userName, password=userPass, email=userMail)
        user.save()
        logger.info(adminNumber)

    form = UserForm()
    context = {'form': form}
    return render(request, 'newUser.html',context)




