import logging
import os
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import *

from app.Dao import daoEvent, analysisDao, MeasureDao
from app.Dao import fileDao
from app.Dao import userDao
from app.Dao.connection import *
from app.form import UserForm
from app.model.analysisMeasure import analysisMeasure as analytic
from app.model.event import event
from app.model.file import file as fichero
from app.model.user import user
from app.model.measure import Measure as measureData
from app.utils import utils

logger = logging.getLogger(__name__)


@login_required(login_url='login/')
def index(request):
    dao = daoEvent.daoEvent()
    list = dao.getEvent(1)
    listUser = dao.getEvent(2)
    context = {'data': list, 'dataUser': listUser}
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
                utils.user = username
                login(request, user)
                return HttpResponseRedirect('/app/')
    return render_to_response('login.html', context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return render_to_response('login.html', context_instance=RequestContext(request))


def measureAdd(request):
    measure = request.GET['measure']
    level = request.GET['level']
    volume = request.GET['volume']
    if float(measure) < 0:
        eventMeausure = event("medida Negativa", 1)
        dao = daoEvent.daoEvent()
        dao.saveEvent(eventMeausure)
    else:
        data = measureData(measure, level, volume, datetime.now())
        dao = MeasureDao()
        dao.saveData(data)


@login_required(login_url='login/')
def measure(request):
    if request.method == 'POST':
        descr = request.POST.get('descr')
        dateInit = request.POST.get('initDate')
        dateEnd = request.POST.get('dateEnd')
        interval = analytic(descr, dateInit, dateEnd)
        dao = analysisDao.analisysDao()
        dao.saveMeasure(interval)

    connec = mongoDB()
    collection = connec.measure()
    data = collection.find()
    length = collection.count()
    context = {'data': data, 'count': length}
    return render(request, 'measure.html', context)


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
        eventMeausure = event("Usuario con nombre: " + name + " ha sido insertado", 2)
        dao = daoEvent.daoEvent()
        dao.saveEvent(eventMeausure)
        newUser.save()
        dao = userDao.daoUser()
        dao.addUser(userAdd)

    form = UserForm()
    context = {'form': form}
    return render(request, 'newUser.html', context)


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
        eventUser = event("Usuario con nombre: " + name + " ha sido modificado", 2)
        dao = daoEvent.daoEvent()
        dao.saveEvent(eventUser)

    return redirect('user')


@login_required(login_url='login/')
def deleteUser(request):
    userGet = request.GET['user']
    userdelete = user(" ", " ", " ", "", userGet, " ", 0)
    dao = userDao.daoUser()
    dao.deleteUser(userdelete)
    eventUser = event("Usuario con nombre: " + userGet + " ha sido eliminado", 2)
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
    return render(request, 'file.html', context)


def handle_uploaded_file(f):
    with open('/Users/sr.kapi/Documents/TFG/mysite/fileUpload/sckech.ino', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
