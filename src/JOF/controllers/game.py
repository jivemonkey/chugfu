# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from JOF.models import Game
from JOF.models import Movie

class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ['movie','user']

def add(request):
    form = GameForm(request.POST)
    if not form.is_valid():
        return render_to_response('game/edit.html',
                                  {'action':'add',
                                   'form': form})

    game = form.save(commit=False)
    game.movie = Movie.objects.get(pk=request.POST['movie_id'])
    if not request.user.is_anonymous() and request.user.is_authenticated():
        game.user = request.user
    game.save()
    return render_to_response('game/detail.html',
                                  {'game' : game,
                                  })

def update(request, game_id):
    game = Game.objects.get(pk=game_id)
    form = GameForm(data=request.POST, instance=game)

    if not form.is_valid():
        return render_to_response('game/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    game = form.save(commit=False)

    if not request.user.is_anonymous() and request.user.is_authenticated():
        game.user = request.user

    game.save()
    return HttpResponseRedirect('/movie/detail/%s' % game.movie.id)

def list(request):
    query = Game.objects.all()
    return render_to_response('game/list.html',
                              {'games': query,
                               'form': GameForm()})

def delete(request, game_id):
    game = Game.objects.get(pk=game_id)
    movie_id = game.movie.id
    game.delete()
    return HttpResponseRedirect('/movie/detail/%s'%movie_id)

def create(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    
    form = GameForm()
    return render_to_response('game/edit.html',
                              {'action':'add',
                               'movie': movie,
                               'form': form})

def edit(request, game_id):
    game = Game.objects.get(pk=game_id)
    form = GameForm(instance=game)
    return render_to_response('game/edit.html',
                              {'action':'update',
                               'movie_id':game.movie.id,
                               'form': form})

def detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    rules = game.rules.all()
    return render_to_response('game/detail.html',
                              {
                                'game': game,
                                'rules': rules
                              })