from django.shortcuts import render
from home import *

# Create your views here.
def index(request):
        return render(request, 'index.html')