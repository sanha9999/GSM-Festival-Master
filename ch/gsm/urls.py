from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register),
    # 즉 , 최종적인 url은 127~~~~:800/user/register가 된다.
]