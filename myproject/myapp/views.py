from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    mydict = {'insertme':'Hi im from the view file in my app!'}
    return render(request,'myapp/index.html',context=mydict)