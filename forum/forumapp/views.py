from django.http import HttpResponse
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
    context = {
        'boards': board_list
    }
    return HttpResponse(template.render(context, request))

def board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('index')
    else:
        form = BoardForm()
    return render(request, 'board.html', { 'form' : form })


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

    context = {
        'category': category,
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def post(request, id):
    template = loader.get_template('post.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def user(request, id):
    template = loader.get_template('user.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def form_add(request, type, id):  # id can be the category pk when creating a post, or the post id when creating a comment
    template = loader.get_template('form.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def form_edit(request, type, id):
    template = loader.get_template('form.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def delete(request, type, id):
    instance = None
    if type == 'post':
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

    return HttpResponseRedirect('/')

def error404(request):
    template = loader.get_template('404.html')
    context = {}
    return HttpResponse(template.render(context, request))