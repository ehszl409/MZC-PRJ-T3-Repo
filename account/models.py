from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password1 = models.EmailField()
    password2 = models.CharField(max_length=100)
    # 다른 필드들을 추가할 수 있습니다
