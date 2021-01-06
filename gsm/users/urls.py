from django.urls import path
from . import views


urlpatterns = [
    path("sign_up", views.sign_up_view, name='sign_up'),
    path("main", views.main_view, name='main'),
    path("sign_in", views.sign_in_view, name="sign_in"),
    path("logout", views.logout_view, name='logout'),

    path('tag/<str:slug>/', views.PostListByTag.as_view()),
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/update/', views.PostUpdate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create/', views.PostCreate.as_view()),
    path('blog/', views.PostList.as_view(), name='blog'),

]