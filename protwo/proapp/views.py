from django.shortcuts import render
from django.http import HttpResponse
from proapp.models import User

# Create your views here.
def index(request):
    return HttpResponse('<em>Hi This is my other app</em>')

def users(request):
    userlist = User.objects.order_by('lastname')
    userdict = {'users':userlist}
    return render(request,'proapp/users.html', context=userdict)

def help(request):
    myhelp = {'halp':'I Need some HAAAAAAALP! HALP!'}
    return render(request,'proapp/help.html',context=myhelp)