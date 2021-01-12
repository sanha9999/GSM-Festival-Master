import random
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User
from .models import Post, Category, Tag, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sklearn.neighbors import KNeighborsClassifier
import joblib
import numpy as np
from scipy.spatial import KDTree
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn import preprocessing

colunm = ["openness", "agreeableness", "emotional_stability", "conscientiousness", "extraversion", "assigned metric", "assigned condition", "is_personalized", "enjoy_watching"]
user = ["user"]
df = pd.DataFrame(index=user, columns=colunm)
# Create your views here.
def question_view(request):

    if request.POST.get('top'):
        df["openness"] = 6.0
        name = 'top'
        print(name)
        return redirect("question2")
    elif request.POST.get('mid'):
        df["openness"] = 4.5
        name = 'mid'
        print(name)
        return redirect("question2")
    elif request.POST.get('mid2'):
        df["openness"] = 3.0
        name = 'mid2'
        print(name)
        return redirect("question2")
    elif request.POST.get('bot'):
        df["openness"] = 2.0
        name = 'bot'
        print(df["openness"])
        return redirect("question2")
    return render(request, "users/question.html")

def question_view2(request):
    if request.POST.get('top'):
        df["agreeableness"] = 6.0
        name = 'top'
        print(name)
        return redirect("question3")
    elif request.POST.get('mid'):
        df["agreeableness"] = 4.5
        name = 'mid'
        print(name)
        return redirect("question3")
    elif request.POST.get('mid2'):
        df["agreeableness"] = 3.0
        name = 'mid2'
        print(name)
        return redirect("question3")
    elif request.POST.get('mid3'):
        df["agreeableness"] = 2.0
        name = 'mid3'
        print(df["openness"])
        return redirect("question3")
    elif request.POST.get('bot'):
        df["agreeableness"] = 1.0
        return redirect("question3")
    return render(request, "users/question2.html")

def question_view3(request):
    if request.POST.get('top'):
        df["emotional_stability"] = 6.0
        name = 'top'
        print(name)
        return redirect("question4")
    elif request.POST.get('mid'):
        df["emotional_stability"] = 4.5
        name = 'mid'
        print(name)
        return redirect("question4")
    elif request.POST.get('mid2'):
        df["emotional_stability"] = 3.0
        name = 'mid2'
        print(name)
        return redirect("question4")
    elif request.POST.get('bot'):
        df["emotional_stability"] = 2.0
        name = 'bot'
        print(df["openness"])
        return redirect("question4")
    return render(request, "users/question3.html")

def question_view4(request):
    if request.POST.get('top'):
        df["conscientiousness"] = 6.0
        name = 'top'
        print(name)
        return redirect("question5")
    elif request.POST.get('mid'):
        df["conscientiousness"] = 4.5
        name = 'mid'
        print(name)
        return redirect("question5")
    elif request.POST.get('mid2'):
        df["conscientiousness"] = 3.0
        name = 'mid2'
        print(name)
        return redirect("question5")
    elif request.POST.get('bot'):
        df["conscientiousness"] = 2.0
        name = 'bot'
        print(df["openness"])
        return redirect("question5")
    return render(request, "users/question4.html")

def question_view5(request):
    if request.POST.get('top'):
        df["extraversion"] = 6.0
        name = 'top'
        print(name)
        return redirect("question6")
    elif request.POST.get('mid'):
        df["extraversion"] = 4.5
        name = 'mid'
        print(name)
        return redirect("question6")
    elif request.POST.get('mid2'):
        df["extraversion"] = 3.0
        name = 'mid2'
        print(name)
        return redirect("question6")
    elif request.POST.get('bot'):
        df["extraversion"] = 2.0
        name = 'bot'
        print(df["openness"])
        return redirect("question6")
    return render(request, "users/question5.html")

def question_view6(request):
    if request.POST.get('top'):
        df["assigned metric"] = 2
        name = 'top'
        print(name)
        return redirect("question7")
    elif request.POST.get('mid'):
        df["assigned metric"] = 1
        name = 'mid'
        print(name)
        return redirect("question7")
    elif request.POST.get('bot'):
        df["assigned metric"] = 0
        name = 'bot'
        print(name)
        return redirect("question7")
    return render(request, "users/question6.html")

def question_view7(request):
    if request.POST.get('top'):
        df["assigned condition"] = 3
        name = 'top'
        print(name)
        return redirect("question8")
    elif request.POST.get('mid'):
        df["assigned condition"] = 2
        name = 'mid'
        print(name)
        return redirect("question8")
    elif request.POST.get('bot'):
        df["assigned condition"] = 1
        name = 'bot'
        print(name)
        return redirect("question8")
    return render(request, "users/question7.html")

def question_view8(request):
    if request.POST.get('top'):
        df["is_personalized"] = 4
        name = 'top'
        print(name)
        return redirect("question9")
    elif request.POST.get('mid'):
        df["is_personalized"] = 3
        name = 'mid'
        print(name)
        return redirect("question9")
    elif request.POST.get('mid2'):
        df["is_personalized"] = 2
        name = 'mid2'
        print(name)
        return redirect("question9")
    elif request.POST.get('mid3'):
        df["is_personalized"] = 1
        name = 'mid3'
        print(df["openness"])
        return redirect("question9")
    elif request.POST.get('bot'):
        df["is_personalized"] = 0
        return redirect("question9")
    return render(request, "users/question8.html")
def question_view9(request):
    if request.POST.get('top'):
        df["enjoy_watching"] = 4
        name = 'top'
        print(name)
        return redirect("question10")
    elif request.POST.get('mid'):
        df["enjoy_watching"] = 3
        name = 'mid'
        print(name)
        return redirect("question10")
    elif request.POST.get('mid2'):
        df["enjoy_watching"] = 2
        name = 'mid2'
        print(name)
        return redirect("question10")
    elif request.POST.get('mid3'):
        df["enjoy_watching"] = 1
        name = 'mid3'
        print(df["openness"])
        return redirect("question10")
    elif request.POST.get('bot'):
        df["enjoy_watching"] = 0
        return redirect("question10")
    return render(request, "users/question9.html")
def question_view10(request):
    if request.method == "POST":
        neigh_model = joblib.load('users/gsmprj.pkl')
        ans = neigh_model.predict(df)
        ans1 = pd.Series(ans)
        ans_val = ans1.values
        rt = int(ans_val)
        if rt < 2:
            return redirect("result1")
        elif rt < 5:
            return redirect("result2")
        elif rt < 7:
            return redirect("result3")
        elif rt < 9:
            return redirect("result4")
        else:
            return redirect("result5")

    return render(request, "users/question10.html")

def sign_up_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["name"]

        user = User.objects.create_user(username, email,  password)
        user.save()
        return redirect("sign_in")
    return render(request, "users/sign-up.html")

def main_view(request):
    return render(request, "users/main.html")

def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
            return render(request, "users/index.html")
        else:
            print("인증 실패")

    return render(request, "users/sign-in.html")


def result_view(request):
    return render(request, "users/result.html")

def result_view2(request):
    return render(request, "users/result2.html")

def result_view3(request):
    return render(request, "users/result3.html")

def result_view4(request):
    return render(request, "users/result4.html")

def result_view5(request):
    return render(request, "users/result5.html")

def logout_view(request):
    logout(request)
    return redirect('sign_in')

def index_view(request):
    return render(request, "users/index.html")


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm()

        return context

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post

    fields = [
        'title', 'content', 'head_image', 'category', 'tags'
    ]

    def form_valid(self, form):
        current_user = self.request.user

        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/blog/')

class PostUpdate(UpdateView):
    model = Post

    fields = [
        'title', 'content', 'head_image', 'category', 'tags'
    ]

class PostListByTag(ListView):
    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=tag_slug)

        return tag.post_set.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        tag_slug = self.kwargs['slug']
        context['tag'] = Tag.objects.get(slug=tag_slug)

        return context

class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']

        if slug == '_none':
            context['category'] = '미분류'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category

        # context['title'] = 'Blog - {}'.format(category.name)
        return context

def new_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.get_absolute_url())
    else:
        return redirect('/blog/')


class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']

        if slug == '_none':
            context['category'] = '미분류'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category

        # context['title'] = 'Blog - {}'.format(category.name)
        return context