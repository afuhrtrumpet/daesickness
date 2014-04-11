from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    t = loader.get_template('home.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def search(request):
	term = request.POST.get('term')
	return HttpRedirectResponse(term)
