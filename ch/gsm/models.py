from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    userid = models.CharField(max_length=64, verbose_name='아이디')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    #저장되는 시점의 시간을 자동으로 삽입해준다.

    def __str__(self):
        return self.username # User object 대신 나타날 문자

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'
