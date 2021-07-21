from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel

# def hello_world(request):             ##request 정보가 적혀있다
#     # 라우팅 : 어떤 주소로 요청을 보내야 해당 view를 작동시킬 것인지 - url
#     # http://       127.0.0.1:8000/     account/hello_world/      ?name=noeul
#     # (통신 프로토콜   서버 주소/IP          페이지 경로                쿼리 데이터)
#     # return HttpResponse('Hello World!')
#     # return render(request, 'base.html')
#     if request.method == "POST":
#
#         temp = request.POST.get('input_text')
#
#         new_model = NewModel()
#         new_model.text = temp
#         new_model.save()
#
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#
#         # data_list = NewModel.objects.all()
#         # return render(request, 'accountapp/hello_world.html',  ## html를 이용한 view
#         #               context={'data_list': data_list})
#                         # context={'text': temp})
#                         # context={'text':'POST METHOD!'})
#     # elif request.method == "GET":
#     else:
#         data_list = NewModel.objects.all()
#         return render(request, 'accountapp/hello_world.html',
#                       context={'data_list': data_list})
#
#     #     # return render(request, 'accountapp/hello_world.html',
#     #     #               context={'text':'GET METHOD!'})

# @login_required(login_url=reverse_lazy('accountapp:login'))    ## accounts가 아니라면 login_url를 적어야한다
@login_required
def hello_world(request):
    # if request.user.is_authenticated:
    if request.method == "POST":
        temp = request.POST.get('input_text')
        new_model = NewModel()
        new_model.text = temp
        new_model.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})
    # else:
    #     return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView): ## generic ~!!!
    model = User                     ## 커스텀 마이징 할 수 있음
    form_class = UserCreationForm    ## 커스텀 마이징 할 수 있음
    success_url = reverse_lazy('accountapp:hello_world')   ## 함수에서는 reverse / 클래스에서는 _lazy 를 써야함 - 불러오는 방식의 차이
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'  # 렌더링은 필요함 -> 라우팅

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm          ## 상속을 만들어서 새로운 클래스 만들어서 회원 아이디 비활성화
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')    # 일단...은... 나중에 detail로 ...
    template_name = 'accountapp/update.html'

    # 클래스 안에 함수는 메서드이기 떄문에 decorotor를 매서드에서 쓸수 있게 해야한다.
    # @login_required
    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:  # self.get_object() = target_user
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #         # return HttpResponseRedirect(reverse('accountapp:login'))

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')    # 탈퇴 후 연결되는 화면
    template_name = 'accountapp/delete.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #         # return HttpResponseRedirect(reverse('accountapp:login'))