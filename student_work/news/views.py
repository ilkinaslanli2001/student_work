from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import News,Category

def homeView(request):

    categories = Category.objects.all()
    news = News.objects.all()

    context = {
        'news': news,
        'categories': categories,
    }

    return render(request, 'news/home.html', context)


def newsView(request,pk):
    categories = Category.objects.all()
    news = News.objects.get(pk=pk)

    context = {
        'news': news,
        'categories': categories,
    }

    return render(request, 'news/news_detail.html', context)

