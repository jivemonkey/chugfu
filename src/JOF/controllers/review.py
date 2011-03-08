# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.forms import ModelForm

from django.http import HttpResponseRedirect

from JOF.models import Review
from JOF.models import Movie

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['movie','user']

def add(request):
    form = ReviewForm(request.POST)
    if not form.is_valid():
        return render_to_response('review/edit.html',
                                  {'action':'add',
                                   'form': form})

    review = form.save(commit=False)
    review.movie = Movie.objects.get(pk=request.POST['movie_id'])
    
    if not request.user.is_anonymous() and request.user.is_authenticated():
        review.user = request.user

    review.save()
    return HttpResponseRedirect('/movie/detail/%s'%request.POST['movie_id'])

def update(request, review_id):
    review = Review.objects.get(pk=review_id)
    form = ReviewForm(data=request.POST, instance=review)

    if not form.is_valid():
        return render_to_response('review/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    review = form.save(commit=False)

    if not request.user.is_anonymous() and request.user.is_authenticated():
        review.user = request.user

    review.save()

    return HttpResponseRedirect('/movie/detail/%s' % review.movie.id)

def list(request):
    query = Review.objects.all()
    return render_to_response('review/list.html',
                              {'reviews': query,
                               'form': ReviewForm()})

def delete(request, review_id):
    review = Review.objects.get(pk=review_id)
    movie_id = review.movie.id
    review.delete()
    return HttpResponseRedirect('/movie/detail/%s'%movie_id)

def create(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    
    form = ReviewForm()
    return render_to_response('review/edit.html',
                              {'action':'add',
                               'movie': movie,
                               'form': form})

def edit(request, review_id):
    review = Review.objects.get(pk=review_id)
    form = ReviewForm(instance=review)
    return render_to_response('review/edit.html',
                              {'action':'update',
                               'id':review_id,
                               'form': form})

def detail(request, review_id):
    review = Review.objects.get(pk=review_id)
    return render_to_response('review/detail.html',
                              {'review': review})