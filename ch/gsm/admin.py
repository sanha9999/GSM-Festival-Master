from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User, UserAdmin) # site에 등록
# admin.ModelAdmin : 상속받게 되면 admin 페이지에서 어떠한 column을 관리할지 등에 대한 설정이 가능
# list_display : 관리자 페이지에서 볼 Column을 넣어주면 된다.