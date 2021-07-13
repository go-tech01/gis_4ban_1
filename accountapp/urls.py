from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp' #주소를 일일이 쓰기 힘드기 때문에 설정

# 127.0.0.1:800/accounts/hellow_world/ =
# acountapp:hello_world     이런 식으로 나중에 대체해서 쓴다 - 라우티

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # name 설정도 주소를 일일이 쓰기 힘드기 때문에 설정
    path('create/', AccountCreateView.as_view(), name='create')
]