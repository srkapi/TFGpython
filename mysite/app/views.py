import logging
from datetime import datetime

from DaoMeause import connection
from  model.user import user
from DaoMeause.connection import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from pymongo import MongoClient
from DaoMeause import userDao
from django.contrib.auth.models import User
from form import UserForm
from models import Measure , Users
from DaoMeause import userDao,connection
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
        else:
            adminBool = False
        userAdd = user(name, lastName, userMail, userPass, userName, adminBool)
        newUser = User.objects.create_user(userName, userPass, userPass)
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
        if admin == '1':
            adminBool = True
        else:
            adminBool = False
        userUpdate = user(name, lastName, userMail, userPass, userName,adminBool)
        dao.updateUser(userUpdate)

    return redirect('user')

@login_required(login_url='login/')
def deleteUser(request):
    user = request.GET.get('user')
    dao = userDao.daoUser()
    dao.deleteUser(user)
    return redirect('user')









