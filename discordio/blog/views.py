from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import *

def index(request):
    articles = Article.objects.all().order_by("-date_published")
    categories = Category.objects.all()
    hot_article = Article.objects.filter(is_hot=True)
    paginator = Paginator(articles, 10)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        articles = paginator.page(page)
    except (InvalidPage, EmptyPage):
        articles = paginator.page(paginator.num_pages)
    
    return render_to_response('timeline.html', dict(articles = articles, hot_article = hot_article, categories=categories))
