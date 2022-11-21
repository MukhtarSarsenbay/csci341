from django.shortcuts import render
from .models import Users

# Create your views here.

def index(request):
    users=Users.objects.all()
    context={
        'users':Users
    }
    return render(request,'index.html',context)


