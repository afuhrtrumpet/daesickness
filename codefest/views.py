from django.template import loader, RequestContext
from django.http import HttpResponse
import parsers.reddit as Reddit
import parsers.healthfinder as HF
import parsers.kaiserhealthnews as KHN
import parsers.medline as ML
from bullentin_board import models

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
    medline = ML.parse(term)
    sources = [healthfinder, kaiserhealthnews, medline, reddit]
    no_results = 0 == sum([len(source['results']) for source in sources])
    c = RequestContext(request, {'sources': sources,
                                 'no_results':no_results,
				 'feedback': [{'message': 'I feel ya',
					 'date': 'today'}],
				 'term': term,
                                 }
                       )
    return HttpResponse(t.render(c))

def submit_feedback(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term')
	message = request.POST.get('message')
	if (BulletinBoard.objects.filter(condition=term).length==0):
		board = models.BulletinBoard(condition=term)
		board.save()
	board.message_set.add(models.Message(message=message))
	c = RequestContext(request, {})
	return HttpResponse(t.render(c))
