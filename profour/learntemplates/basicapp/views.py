from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'helloworld','number':100}
    return render(request,'basicapp/index.html',context=context_dict)

def other(request):
    return render(request,'basicapp/other.html')

def mytest(request):
    return render(request,'basicapp/mytest.html')