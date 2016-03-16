from django.http import HttpResponse
from models import Post,Measure

def index(request):
    post = Measure.objects.create( sensor='arduino', type=2,value=0)
    post.save()
    return HttpResponse("Hello, world. You're at the polls index.")# Create your views here.
