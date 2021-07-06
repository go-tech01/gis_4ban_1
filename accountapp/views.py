from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):             ##request 정보가 적혀있다
    # return HttpResponse('Hello World!')
    # return render(request, 'base.html')
    return render(request, 'accountapp/hello_world.html')