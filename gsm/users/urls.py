from django.urls import path
from . import views


urlpatterns = [
    path("sign_up", views.sign_up_view, name='sign_up'),
    path("main", views.main_view, name='main'),
    path("sign_in", views.sign_in_view, name="sign_in"),
    path("logout", views.logout_view, name='logout'),
    path("question", views.question_view, name='question'),
    path("question2", views.question_view2, name='question2'),
    path("question3", views.question_view3, name='question3'),
    path("question4", views.question_view4, name='question4'),
    path("question5", views.question_view5, name='question5'),
    path("question6", views.question_view6, name='question6'),
    path("question7", views.question_view7, name='question7'),
    path("question8", views.question_view8, name='question8'),
    path("question9", views.question_view9, name='question9'),
    path("question10", views.question_view10, name='question10'),
    path("result1", views.result_view, name='result1'),
    path("result2", views.result_view2, name='result2'),
    path("result3", views.result_view3, name='result3'),
    path("result4", views.result_view4, name='result4'),
    path("result5", views.result_view5, name='result5'),
    path("index", views.index_view, name='index'),


    path('tag/<str:slug>/', views.PostListByTag.as_view()),
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/update/', views.PostUpdate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create/', views.PostCreate.as_view()),
    path('blog/', views.PostList.as_view(), name='blog'),

]