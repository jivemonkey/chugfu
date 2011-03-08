#User views
from django.forms import ModelForm

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User

def add(request):

    form = UserForm(request.POST)

    if not form.is_valid():
        return render_to_response('user/edit.html',
                                  {'action':'add','form': form})
    
    user = User.objects.filter(username=request.POST['username']).count()

    if user > 0:
        form.errors['User Already Exists'] = "- A user with this username already exists"
        return render_to_response('user/edit.html',
                          {'action':'add','form': form})
        
    user = form.save(commit=False)
    user.save()

    return HttpResponseRedirect('/')

def list(request):
    query = User.objects.all()
    return render_to_response('user/list.html',
                              {'users': query,
                               'form': UserForm()})

def create(request):
    form = UserForm()
    return render_to_response('user/edit.html',
                              {'action':'add','form': form})

def edit(request, user_id):
    user = User.objects.get(user_id)
    form = UserForm(instance=user)
    return render_to_response('user/edit.html',
                              {'action':'update',
                               'form': form})

def detail(request, user_id):
    user = User.objects.get(user_id)

    return render_to_response('user/detail.html',
                              {'user': user})

def delete(request, user_id):
    User.objects.get(user_id).delete()
    return HttpResponseRedirect('/')