from django.shortcuts import render
from . import forms as myforms
# Create your views here.
def index(request):
    return render(request, 'applvl3/index.html')

def formview(request):
    form = myforms.MyForm()
    if request.method == 'POST':
        form = myforms.MyForm(request.POST)
        if form.is_valid():
            print('Validation successful!')
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request,'applvl3/forms.html',{'form':form})

def comingsoon(request):
    form = myforms.LandForm()
    if request.method == 'POST':
        form = myforms.LandForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('error form invalid')
    return render(request,'applvl3/comingsoon.html',{'form':form})