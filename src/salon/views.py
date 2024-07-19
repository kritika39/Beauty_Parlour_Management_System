from django.shortcuts import render,redirect
from django.http import HttpResponse 




def index(request):
    #  return HttpResponse('this is about us page')
        
    return render(request,'salon/index.html')

def service(request):
    return render(request,'salon/service.html')

