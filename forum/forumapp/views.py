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

def category(request):
    template = loader.get_template('category.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def post(request):
    template = loader.get_template('post.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))

def user(request):
    template = loader.get_template('user.html')
    context = {}  # TODO: add contexts
    return HttpResponse(template.render(context, request))