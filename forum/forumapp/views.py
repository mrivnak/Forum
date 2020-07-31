from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.contrib.auth import login as authlogin, authenticate

from .forms import *
from .models import *

# Create your views here.
def index(request):
    template = loader.get_template('index.html')

    boards = Board.objects.order_by()
    board_list = []

    for board in boards:
        categories = board.category_set.all()

        category_list = []

        for category in categories:
            category_list.append({
                'category': category,
                'id': category.pk
            })

        board_list.append({
            'board': board,
            'categories': category_list
        })
    
    zoom_list = Zoom.objects.order_by()

    context = {
        'boards': board_list,
        'zoom_list': zoom_list,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            authlogin(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', { 'form' : form })

def category(request, id):
    template = loader.get_template('category.html')

    category = Category.objects.get(pk=id)
    posts = category.post_set.all()

    zoom_list = Zoom.objects.order_by()

    context = {
        'category': category,
        'posts': posts,
        'zoom_list': zoom_list,
    }
    return HttpResponse(template.render(context, request))

def post(request, id):
    template = loader.get_template('post.html')

    post = Post.objects.get(pk=id)

    zoom_list = Zoom.objects.order_by()

    comments = post.comment_set.all()

    form = CommentForm()

    context = {
        'post': post,
        'zoom_list': zoom_list,
        'comments': comments,
        'form': form,
    }  # TODO: add contexts


    return HttpResponse(template.render(context, request))

def user(request, id):
    template = loader.get_template('user.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def form_add(request, type):  # id can be the category pk when creating a post, or the post id when creating a comment
    form = None

    if request.method == 'POST':
        if type == 'board':
            form = BoardForm(request.POST)
        else:
            return HttpResponseNotFound("Invalid form option(s)")

        if form.is_valid():
            form.save()
            return redirect('/')

    elif request.method == 'GET':
        if type == 'board':
            form = BoardForm()
        else:
            return HttpResponseNotFound("Invalid form option(s)")

        template = loader.get_template('form.html')

        context = {
            'request': request,
            'type': type,
            'title': type.title(),
            'form': form,
        }  # TODO: add contexts

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponseNotFound("Invalid form option(s)")

def form_add_id(request, type, id):  # id can be the category pk when creating a post, or the post id when creating a comment
    form = None

    if request.method == 'POST':
        if type == 'category':
            form = CategoryForm(request.POST)

            if form.is_valid():
                category = form.save(commit=False)
                category.Board = Board.objects.get(pk=id)
                category.save()
                return redirect('/')
        elif type == 'post':
            form = PostForm(request.POST)

            if form.is_valid():
                post = form.save(commit=False)
                post.Category = Category.objects.get(pk=id)
                post.User = request.user
                post.save()
                post_id = post.PostID
                return redirect(f'/post/{post_id}')
        elif type == 'comment':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.Post = Post.objects.get(pk=id)
                comment.User = request.user
                comment.save()
                return redirect(f'/post/{id}')
        else:
            return HttpResponseNotFound("Invalid form option(s)")

    elif request.method == 'GET':
        if type == 'category':
            form = CategoryForm()
        elif type == 'post':
            form = PostForm()
        elif type == 'comment':
            form = CommentForm()
        else:
            return HttpResponseNotFound("Invalid form option(s)")

        template = loader.get_template('form.html')

        context = {
            'request': request,
            'type': type,
            'title': type.title(),
            'form': form,
        }  # TODO: add contexts

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponseNotFound("Invalid form option(s)")

def form_edit(request, type, id):
    template = loader.get_template('form.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def delete(request, type, id):
    instance = None
    if type == 'board':
        instance = Board.objects.get(pk=id)
        instance.delete()
    elif type == 'category':
        instance = Category.objects.get(pk=id)
        instance.delete()
    elif type == 'post':
        instance = Post.objects.get(pk=id)
        instance.delete()
    elif type == 'user':
        instance = User.objects.get(pk=id)
        instance.delete()
    elif type == 'comment':
        instance = Comment.objects.get(pk=id)
        instance.delete()
    else:
        return HttpResponseNotFound("Invalid form option(s)")

    return redirect('/')

def page_not_found(request, exception):
    template = loader.get_template('404.html')
    context = {
        'exception': exception
    }
    return HttpResponse(template.render(context, request))