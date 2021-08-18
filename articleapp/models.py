from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # on_delete=models.CASCADE 유저가 탈퇴하면 삭제됨, SET_NULL 게시판이 누군지 모르겠다
    # target_user.article
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    # 장문은 TextField
    created_at = models.DateField(auto_now_add=True, null=True)

