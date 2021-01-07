import random

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User
from .models import Post, Category, Tag, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def question_view(request):
    return render(request, "users/question.html")

def question_view2(request):
    return render(request, "users/question2.html")

def question_view3(request):
    return render(request, "users/question3.html")

def question_view4(request):
    return render(request, "users/question4.html")

def question_view5(request):
    return render(request, "users/question5.html")

def question_view6(request):
    return render(request, "users/question6.html")

def question_view7(request):
    return render(request, "users/question7.html")

def question_view8(request):
    return render(request, "users/question8.html")
def question_view9(request):
    return render(request, "users/question9.html")
def question_view10(request):
    if request.method == "POST":
        number = random.randrange(1, 6)
        if number == 1:
            return redirect('result1')
        elif number == 2:
            return redirect('result2')
        elif number == 3:
            return redirect('result3')
        elif number == 4:
            return redirect('result4')
        else:
            return redirect('result5')
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