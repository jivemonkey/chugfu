# Create your views here.
from django.shortcuts import render_to_response
from django.forms import ModelForm

from django.http import HttpResponseRedirect

from JOF.models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie

def add(request):
    form = MovieForm(request.POST)
    if not form.is_valid():
        return render_to_response('movie/edit.html',
                                  {'action':'add',
                                   'form': form})

    movie = form.save(commit=False)
    movie.save()
    
    return HttpResponseRedirect('/movie/list') #list(request)

def update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    form = MovieForm(data=request.POST, instance=movie)

    if not form.is_valid():
        return render_to_response('movie/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    movie = form.save(commit=False)
    movie.save()
    return detail(request, movie_id)

def list(request):
    query = Movie.objects.all()
    if 'user' in request.session.keys():
        user = request.session['user']
    else:
        user = {}
    return render_to_response('movie/list.html',
                              {'user':user,'movies': query,
                               'form': MovieForm()})

def delete(request, movie_id):
    Movie.objects.get(pk=movie_id).delete()
    return list(request)

def create(request):
    form = MovieForm()
    return render_to_response('movie/edit.html',
                              {'action':'add',
                               'form': form})

def edit(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    form = MovieForm(instance=movie)
    return render_to_response('movie/edit.html',
                              {'action':'update',
                               'id':movie_id,
                               'form': form})

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    reviews = movie.reviews.all()
    games = movie.games.all()

    if 'user' in request.session.keys():
        user = request.session['user']
    else:
        user = {}
    return render_to_response('movie/detail.html',
                              {'user':user,
                               'reviews': reviews,
                               'games': games,
                               'movie': movie})

def index(request):
    return list(request)