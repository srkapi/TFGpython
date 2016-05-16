
from datetime import datetime
import os

from django.core.files.base import ContentFile

from mysite import settings
from DaoMeause import connection
from model.user import user
from model.event import event
from model.file import file as fichero
from DaoMeause.connection import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from pymongo import MongoClient
from DaoMeause import daoEvent,userDao
from DaoMeause import fileDao
from django.contrib.auth.models import User
from form import UserForm
from models import Measure , Users
from DaoMeause import userDao,connection
import logging
logger = logging.getLogger(__name__)



@login_required(login_url='login/')
def index(request):
    dao = daoEvent.daoEvent()
    list = dao.getEvent(1)
    listUser = dao.getEvent(2)
    context = {'data':  list ,'dataUser':  listUser}
    return render(request, 'event.html', context)



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
    if float(measure) < 0:
        eventMeausure = event("medida Negativa",1)
        dao = daoEvent.daoEvent()
        dao.saveEvent(eventMeausure)
        return HttpResponse("medida negativa")# Create your views here.
    else:
        post = Measure.objects.create(sensor=sensor, type=2, value=measure, fecha=datetime.now())
        post.save()
        return HttpResponse("medida insertada con exist")# Create your views here.

@login_required(login_url='login/')
def measure(request):
    connec = mongoDB()
    collection = connec.measure()
    data = collection.find()
    length = collection.count()
    context = {'data':  data ,'count': length}

    return render(request, 'measure.html',context)

@login_required(login_url='login/')
def list_user(request):
    dao = userDao.daoUser()
    list = dao.getAll()
    context = {'data': list}
    return render(request, 'user.html', context)


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
            adminBool = True
            newUser = User.objects.create_superuser(userName, userMail, userPass)
        else:
            adminBool = False
            newUser = User.objects.create_user(userName, userPass, userMail)

        userAdd = user(name, lastName, userMail, userPass, userName, adminBool, 1)
        eventMeausure = event("Usuario con nombre: "+name +" ha sido insertado", 2)
        dao = daoEvent.daoEvent()
        dao.saveEvent(eventMeausure)
        newUser.save()
        dao = userDao.daoUser()
        dao.addUser(userAdd)

    form = UserForm()
    context = {'form': form}
    return render(request, 'newUser.html',context)

@login_required(login_url='login/')
def updateUser(request):
    dao = userDao.daoUser()
    if request.method == 'POST':
        userName = request.POST.get('user')
        userPass = request.POST.get('pass')
        userMail = request.POST.get('email')
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        admin = request.POST.get('admin')
        activo = request.POST.get('activo')
        if admin == '1':
            adminBool = True
        else:
            adminBool = False

        userUpdate = user(name, lastName, userMail, userPass, userName, adminBool, int(activo))
        dao.updateUser(userUpdate)
        eventUser = event("Usuario con nombre: "+name +" ha sido modificado", 2)
        dao = daoEvent.daoEvent()
        dao.saveEvent(eventUser)

    return redirect('user')



@login_required(login_url='login/')
def deleteUser(request):
    userGet = request.GET['user']
    userdelete = user(" ", " ", " ", "", userGet," ",0)
    dao = userDao.daoUser()
    dao.deleteUser(userdelete)
    eventUser = event("Usuario con nombre: "+userGet +" ha sido eliminado", 2)
    dao = daoEvent.daoEvent()
    dao.saveEvent(eventUser)
    return redirect('user')

def file(request):

    if request.method == 'POST':
       # folder = request.path.replace("/", "_")
        uploaded_filename = request.FILES['file'].name
        if os.path.isfile('/Users/sr.kapi/Documents/TFG/mysite/fileUpload/sckech.ino') == True:
            os.remove('/Users/sr.kapi/Documents/TFG/mysite/fileUpload/sckech.ino')
        handle_uploaded_file(request.FILES['file'])
        # create the folder if it doesn't exist.


        newFile = fichero(uploaded_filename)
        dao = fileDao.fileDao()
        dao.saveFile(newFile)

    dao = fileDao.fileDao()
    list = dao.getAll()
    context = {'data': list}
    return render(request, 'file.html',context)



def handle_uploaded_file(f):
    with open('/Users/sr.kapi/Documents/TFG/mysite/fileUpload/sckech.ino', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)









