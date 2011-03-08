# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import *

urlpatterns = patterns('JOF.controllers',
    # Main page
    (r'^$','views.index'),
    # Movies Actions
    (r'^movie/list/$','movie.list'),
    (r'^movie/edit/(?P<movie_id>\w+)/$','movie.edit'),
    (r'^movie/add/$','movie.add'),
    (r'^movie/update/(?P<movie_id>\w+)$','movie.update'),
    (r'^movie/detail/(?P<movie_id>\w+)/$','movie.detail'),
    (r'^movie/create/$','movie.create'),
    (r'^movie/delete/(?P<movie_id>\w+)/$','movie.delete'),
    # Review Actions
    (r'^review/list/$','review.list'),
    (r'^review/edit/(?P<review_id>\w+)/$','review.edit'),
    (r'^review/add/$','review.add'),
    (r'^review/update/(?P<review_id>\w+)$','review.update'),
    (r'^review/detail/(?P<review_id>\w+)/$','review.detail'),
    (r'^review/create/(?P<movie_id>\w+)/$','review.create'),
    (r'^review/delete/(?P<review_id>\w+)/$','review.delete'),
    # Game Actions
    (r'^game/list/$','game.list'),
    (r'^game/edit/(?P<game_id>\w+)/$','game.edit'),
    (r'^game/add/$','game.add'),
    (r'^game/update/(?P<game_id>\w+)$','game.update'),
    (r'^game/detail/(?P<game_id>\w+)/$','game.detail'),
    (r'^game/create/(?P<movie_id>\w+)/$','game.create'),
    (r'^game/delete/(?P<game_id>\w+)/$','game.delete'),
    # Game Rule Actions
    (r'^rule/add/$','rule.add'),
    (r'^rule/delete/(?P<rule_id>\w+)/$','rule.delete'),
    # News Actions
    (r'^news/list/$','news.list'),
    (r'^news/edit/(?P<news_id>\w+)/$','news.edit'),
    (r'^news/add/$','news.add'),
    (r'^news/update/(?P<news_id>\w+)$','news.update'),
    (r'^news/create/$','news.create'),
    (r'^news/delete/(?P<news_id>\w+)/$','news.delete'),
    # User Actions
    (r'^user/list/$','user.list'),
    (r'^user/edit/(?P<user_id>\w+)/$','user.edit'),
    (r'^user/detail/(?P<user_id>\w+)/$','user.detail'),
    (r'^user/add/$','user.add'),
    (r'^user/create/$','user.create'),
    (r'^user/delete/(?P<user_id>\w+)/$','user.delete'),
)
urlpatterns += patterns('',
    # Django User Actions
    #(r'^user/login/$', 'django.contrib.auth.views.login', {'template_name': 'user/login.html'}),
    (r'^user/login/$', 'django.contrib.auth.views.login', {"template":"user/login.html", "next_url":"/"}),
    (r'^user/logout/$', 'django.contrib.auth.views.logout', {'next_url': '/'}),
    (r'^user/register/$', 'django.contrib.auth.views.register', {"template":"user/register.html", "next_url":"/"}),
)
