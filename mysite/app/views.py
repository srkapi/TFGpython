from django.http import HttpResponse
from models import Post,Measure

def index(request):
    post = Measure.objects.create( sensor='arduino', type=2,value=0)
    post.save()
    return HttpResponse("Hello, world. You're at the polls index.")# Create your views here.



def measure(request):
    sensor=request.GET['sensor']
    measure=request.GET['measure']
    post = Measure.objects.create( sensor=sensor, type=2,value=measure)
    post.save()
    return HttpResponse("medida insertada con exist")# Create your views here.
