from django.template import loader, RequestContext
from django.http import HttpResponse
import parsers.reddit as Reddit
import parsers.healthfinder as HF

def home(request):
    t = loader.get_template('home.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def search(request):
    t = loader.get_template('results.html')
    term = request.POST.get('term')
    reddit = Reddit.parse(term)
    healthfinder = HF.parse(term)
    sources = [reddit,healthfinder]
    c = RequestContext(request, {'sources': sources})
    return HttpResponse(t.render(c))
