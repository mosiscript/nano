from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import SendAticleForm
from .models import Article


def index(request):

    articles = Article.objects.order_by('-created_at')
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'articles/index.html', {
        'title' : 'Article Page',
        'articles' : articles,
        'paginator' : paginator
    })

def single(request, article_id):

    article = Article.objects.get(id = article_id)

    return render(request, 'articles/single.html' , {
        'title' : article.title ,
        'article' : article
    })

@login_required
def send(request):
    if request.method == 'POST':
        form = SendAticleForm(request.POST)

        if form.is_valid():
            Article.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                published_at = form.cleaned_data['published_at']
            )

            return redirect('articles:articles')

    else:
        form = SendAticleForm()

    return render(request, 'articles/send.html', {'form':form})


# ================ edit =================================
def edit(request, article_id):
    article = get_object_or_404(Article, id = article_id)

    if request.method == 'POST':
        form = SendAticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.published_at = form.cleaned_data['published_at']

            article.save()

        return redirect('articles:articles')

    else:
        form = SendAticleForm()
        #  if we use {{title}} instead of <input> then :
        #  form = SendArticleForm('title':article.title, 'body':article.body , ...) OR SendArticleForm(article.__dict__)
        #  see video 30 of roocket tutorial

    return render(request, 'articles/edit.html', {'form':form, 'article':article})













# def send(request):
#     if request.method == 'GET':
#         return render(request, 'articles/send.html')
#     else:
#         return HttpResponseNotAllowed('GET')

# def store(request):
#     if request.method == 'POST':
#         return HttpResponse(request.POST.get('title'))
#     else:
#         return HttpResponseNotAllowed('POST')

# def send(request):
#     if request.method == 'POST':
#         return HttpResponse(request.POST.get('title'))
#     else:
#         return render(request, 'articles/send.html')
