from django.template import loader, RequestContext
from django.http import HttpResponse
import parsers.reddit as Reddit
import parsers.healthfinder as HF
import parsers.kaiserhealthnews as KHN

def home(request):
    t = loader.get_template('home.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def search(request):
    t = loader.get_template('results.html')
    term = request.POST.get('term')
    reddit = Reddit.parse(term)
    healthfinder = HF.parse(term)
    kaiserhealthnews = KHN.parse(term)
    sources = [reddit,healthfinder, kaiserhealthnews]
    c = RequestContext(request, {'sources': sources})
    return HttpResponse(t.render(c))
