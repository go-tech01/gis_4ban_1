from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel

from articleapp.models import Article

class AccountCreateView(CreateView): ## generic ~!!!
    model = User                     ## 커스텀 마이징 할 수 있음
    form_class = UserCreationForm    ## 커스텀 마이징 할 수 있음
    success_url = reverse_lazy('articleapp:list')   ## 함수에서는 reverse / 클래스에서는 _lazy 를 써야함 - 불러오는 방식의 차이
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'  # 렌더링은 필요함 -> 라우팅

    paginate_by = 8

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)

has_ownership = [login_required, account_ownership_required]

# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm          ## 상속을 만들어서 새로운 클래스 만들어서 회원 아이디 비활성화
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})


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


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')    # 탈퇴 후 연결되는 화면
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