from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm, loginForm
from .models import articleModel, loginModel

def home(request):
    articles = articleModel.objects.all().order_by('-id')
    context = {
    'last_art': articles[0],
    'second_last_art': articles[1],
    'third_last_art': articles[2],
    'fourth_last_art': articles[3]
    }
    return render(request, 'Home.html', context)

def article(request, id_article):
    article = articleModel.objects.get(id=id_article)
    return render(request, 'article.html', {"article":article})

@login_required()
def getArticle(request):
    context = {}
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            img = form.cleaned_data.get('img')
            body = form.cleaned_data.get('body')
            obj = articleModel.objects.create(title=title, img=img, body=body)
            obj.save()
            return redirect('/')
    else:
        form = ArticleForm()
    context['form'] = form
    return render(request, 'form.html', context)

def logging(request):
    context = {}
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post')
    else:
        form = loginForm()
    context['form'] = form
    return render(request, 'login.html', context)