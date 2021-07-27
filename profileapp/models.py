from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')  # 연결해주는 필드
    # 삭제가 되었을때 행동하는 것 정의해주기 : cascade - 종속 - user가 삭제되면 profile도 삭제해라 (SET_NULL 하면 삭제하지 않는다?)
    # 유저 객체가 user.profile 이런 식으로 접근하기 위해
    image = models.ImageField(upload_to='profile/', null=True)
    # upload_to -> 이미지을 받았을때 저장하는 경로 / null=True 이미지 없어도 프로필 만들수 있게
    nickname = models.CharField(max_length=30, unique=True, null=True)
    # 최대 글자 및 중복 할 수 없게 설정
    message = models.CharField(max_length=200, null=True)
