from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import NewModel


def hello_world(request):             ##request 정보가 적혀있다
    # 라우팅 : 어떤 주소로 요청을 보내야 해당 view를 작동시킬 것인지 - url
    # http://       127.0.0.1:8000/     account/hello_world/      ?name=noeul
    # (통신 프로토콜   서버 주소/IP          페이지 경로                쿼리 데이터)
    # return HttpResponse('Hello World!')
    # return render(request, 'base.html')
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

        # data_list = NewModel.objects.all()
        # return render(request, 'accountapp/hello_world.html',  ## html를 이용한 view
        #               context={'data_list': data_list})
                        # context={'text': temp})
                        # context={'text':'POST METHOD!'})
    # elif request.method == "GET":
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})

        # return render(request, 'accountapp/hello_world.html',
        #               context={'text':'GET METHOD!'})
