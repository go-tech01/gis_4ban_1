from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'

#profileapp:create

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
]
