from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import parsers.reddit as Reddit

def home(request):
    t = loader.get_template('home.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def search(request):
	t = loader.get_template('results.html')
	term = request.POST.get('term')
	redditResults = Reddit.parse(term)
	c = RequestContext(request, {'reddit': redditResults})
	return HttpResponse(t.render(c))
