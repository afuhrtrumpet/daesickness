from django.template import loader, RequestContext
from django.http import HttpResponse

def home(request):
    t = loader.get_template('home.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))