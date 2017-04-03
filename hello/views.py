from django.http import HttpResponse
from random import *

# Create your views here.
randNum = randint(1, 100);

def index(request):
        return HttpResponse("Hello, DJango World! Your lucky number is " + str(randNum))
