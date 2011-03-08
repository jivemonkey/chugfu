# Create your views here.
from django.shortcuts import render_to_response
from google.appengine.ext import db

from JOF import models

def index(request):
    query = models.News.objects.all()
    
    if 'user' in request.session.keys():
        user = request.session['user']
    else:
        user = {}
    
    return render_to_response('index.html',
                              {'user':user,'news': query})
