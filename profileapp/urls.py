from django.urls import path

from profileapp.views import ProfileCreatView

app_name = 'profileapp'

#profileapp:create

urlpatterns = [
    path('create/', ProfileCreatView.as_view(), name='create'),
]
