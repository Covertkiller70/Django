from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<em>Hi This is my other app</em>')

def help(request):
    myhelp = {'halp':'I Need some HAAAAAAALP! HALP!'}
    return render(request,'proapp/help.html',context=myhelp)