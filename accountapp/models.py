from django.db import models

# Create your models here.




# 장고에서 기본적으로 제공해주는 모델을 상속 받는다
class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False)        ## 이text는 문자열을 받을 것이다
