from django.template import loader, RequestContext
from django.http import HttpResponse
import parsers.reddit as Reddit
import parsers.healthfinder as HF
import parsers.kaiserhealthnews as KHN
import parsers.medline as ML
from bulletin_board import models

def home(request, returning=False):
	t = loader.get_template('home.html')
	c = RequestContext(request, {'purpose':'home'})
	return HttpResponse(t.render(c))

def search(request):
	t = loader.get_template('results.html')
	term = request.POST.get('term').lower()
	reddit = Reddit.parse(term)
	healthfinder = HF.parse(term)
	kaiserhealthnews = KHN.parse(term)
	medline = ML.parse(term)
	sources = [healthfinder, kaiserhealthnews, medline, reddit]
	feedback = []
	if len(models.BulletinBoard.objects.filter(condition=term)) != 0:
		feedback = models.BulletinBoard.objects.filter(condition=term)[0].message_set.all()
	no_results = 0 == sum([len(source['results']) for source in sources])
	c = RequestContext(request, {'purpose':'search_results',
                                 'sources': sources,
								 'no_results':no_results,
								'feedback': feedback,
								'term': term,
								 }
					   )
	return HttpResponse(t.render(c))

def submit_feedback(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term').lower()
	message = request.POST.get('message')
	if len(models.BulletinBoard.objects.filter(condition=term)) == 0:
		board = models.BulletinBoard(condition=term)
		board.save()
	else:
		board = models.BulletinBoard.objects.filter(condition=term)[0]
	board.message_set.add(models.Message(message=message))
	c = RequestContext(request, {'purpose':'successful_feedback'})
	return HttpResponse(t.render(c))
