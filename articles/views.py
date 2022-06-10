from datetime import date
from django.shortcuts import redirect, render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == 'POST':
        form = forms.createArticle(request.POST, request.FILES)
        if form.is_valid():
            test1 = form.save(commit=False)
            test1.author = request.user
            test1.save()
            redirect('articles:list')
    else:
        form = forms.createArticle()
        return render(request, 'articles/create_article.html', {'form': form})
