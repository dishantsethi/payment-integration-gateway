from django.shortcuts import render
from django.http import HttpResponse

def pay(request):
    return render(request,'pay.html')
