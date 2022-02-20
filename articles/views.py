from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    
    # return HttpResponse(slug)

    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method != 'POST':
        form = forms.CreateArticle(instance=article)
        
    else:
        form = forms.CreateArticle(instance=article, data=request.POST, files=request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    
    context = {'article': article, 'form': form}

    return render(request, 'articles/edit_article.html', context)

