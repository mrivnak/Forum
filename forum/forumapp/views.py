from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def category(request, id):
    template = loader.get_template('category.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def post(request, id):
    template = loader.get_template('post.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def user(request, id):
    template = loader.get_template('user.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def form_add(request, type):
    template = loader.get_template('user.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def form_edit(request, type, id):
    template = loader.get_template('user.html')
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
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))