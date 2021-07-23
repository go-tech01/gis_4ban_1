

from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# 계정소유권이 필요하다
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated