# Create your views here.
import urllib2
from django.http import HttpResponse

def get(request, image_url):

    req = urllib2.Request(image_url)
    req.add_header('Referer', "http://www.imdb.com")
    r = urllib2.urlopen(req)

    return HttpResponse(r, mimetype="image/jpg")
