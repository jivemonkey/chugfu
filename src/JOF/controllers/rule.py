# Create your views here.
from django.contrib.auth.models import User
from django.forms import ModelForm

from django.http import HttpResponse

from JOF.models import Game
from JOF.models import GameRule

class RuleForm(ModelForm):
    class Meta:
        model = GameRule
        exclude = ['movie','user']

def add(request):
    form = RuleForm(request.POST)

    if not form.is_valid():
        return HttpResponse(form,status=400)
    
    rule = form.save(commit=False)

    rule.game = Game.objects.get(pk=request.POST['game_id'])
    
    if not request.user.is_anonymous() and request.user.is_authenticated():
        rule.user = request.user

    rule.save()

    data = '{"desc": "%s", "points": "%s", "id":"%s"}' % (rule.description, rule.points, rule.id)
    return HttpResponse(data, 'application/javascript')

def update(request, game_id):
    rule = GameRule.objects.get(pk=game_id)
    form = RuleForm(request.POST, instance=rule)
    
    if not form.is_valid():
        return HttpResponse(status=400)
    
    rule = form.save(commit=False)

    rule.game = Game.objects.get(pk=request.POST['game_id'])
    
    if not request.user.is_anonymous() and request.user.is_authenticated():
        rule.user = request.user

    key = rule.save()

    data = '{"desc": "%s", "points": "%d", "key":"%s"}' % (rule.description, rule.points, str(key))
    return HttpResponse(data, 'application/javascript')

def delete(request, rule_id):
    GameRule.objects.get(pk=rule_id).delete()

    return HttpResponse('success')