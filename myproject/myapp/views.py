from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import AccessRecord,Webpage,Topic

# Create your views here.
def index(request):
    weblist = AccessRecord.objects.order_by('date')
    datedict = {'accessrecords':weblist}
    return render(request,'myapp/index.html', context=datedict)

def view(request):
    mydict = {'insertme':'Hi im from the view file in my app!'}
    return render(request,'myapp/index.html',context=mydict)

def home(request):
    mydict = {'insertme':'Hello from the homescreen!'}
    return render(request,'myapp/index.html', context=mydict)