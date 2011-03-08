# Create your views here.
from django.shortcuts import render_to_response
from django.forms import ModelForm

from JOF import models

class NewsForm(ModelForm):
    class Meta:
        model = models.News

def add(request):
    form = NewsForm(request.POST)
    if not form.is_valid():
        return render_to_response('news/edit.html',
                                  {'action':'add',
                                   'form': form})

    news = form.save(commit=False)
    news.save()
    return list(request)

def update(request, news_id):
    news = models.News.objects.get(pk=news_id)
    form = NewsForm(data=request.POST, instance=news)

    if not form.is_valid():
        return render_to_response('news/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    news = form.save(commit=False)
    news.save()
    return list(request)

def list(request):
    query = models.News.objects.all()
    return render_to_response('news/list.html',
                              {'news': query})

def delete(request, news_id):
    models.News.objects.get(news_id).delete()
    return list(request)

def create(request):
    form = NewsForm()
    return render_to_response('news/edit.html',
                              {'action':'add',
                               'form': form})

def edit(request, news_id):
    news = models.News.objects.get(pk=news_id)
    form = NewsForm(instance=news)
    return render_to_response('news/edit.html',
                              {'action':'update',
                               'id':news_id,
                               'form': form})