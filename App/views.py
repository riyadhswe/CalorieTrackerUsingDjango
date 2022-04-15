from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    foods = Food.objects.all()

    contex = {
        'foods' : foods
    }

    return render(request,'index.html',contex)
