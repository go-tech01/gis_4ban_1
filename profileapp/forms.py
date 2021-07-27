from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:  ## 메타 클래식 지정
# -> 메타정보 : 이미지의 대상은 이미지 안에 있는 픽셀데이터다,
# 메타데이터는 그 이미지 말고 그 이미지의 주변 정보들, 어떤 카메카로 찍었는지...기타 등등 외부 정보...
        model = Profile
        fields = ['image', 'nickname', 'message']
