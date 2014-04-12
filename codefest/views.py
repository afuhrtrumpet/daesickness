from django.template import loader, RequestContext
from django.http import HttpResponse
import parsers.reddit as Reddit
import parsers.healthfinder as HF
import parsers.kaiserhealthnews as KHN
import parsers.medline as ML
from bulletin_board.models import BulletinBoard, Message
from buddy.models import Buddy

def home(request, returning=False):
	t = loader.get_template('home.html')
	c = RequestContext(request, {'purpose':'home'})
	return HttpResponse(t.render(c))

def search(request):
<<<<<<< HEAD
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
=======
    t = loader.get_template('results.html')
    term = request.POST.get('term').lower()
    reddit = Reddit.parse(term)
    healthfinder = HF.parse(term)
    kaiserhealthnews = KHN.parse(term)
    medline = ML.parse(term)
    sources = [healthfinder, kaiserhealthnews, medline, reddit]
    feedback = []
    if len(BulletinBoard.objects.filter(condition=term))!=0:
	    feedback = BulletinBoard.objects.filter(condition=term)[0].message_set.all()
    no_results = 0 == sum([len(source['results']) for source in sources])
    c = RequestContext(request, {'sources': sources,
                                 'no_results':no_results,
                                'feedback': feedback,
                                'term': term,
                                 }
                       )
    return HttpResponse(t.render(c))
>>>>>>> f95383134eb067817e052f966e11f86b64172c46

def submit_feedback(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term').lower()
	message = request.POST.get('message')
<<<<<<< HEAD
	if len(models.BulletinBoard.objects.filter(condition=term)) == 0:
		board = models.BulletinBoard(condition=term)
=======
	if len(BulletinBoard.objects.filter(condition=term))==0:
		board = BulletinBoard(condition=term)
>>>>>>> f95383134eb067817e052f966e11f86b64172c46
		board.save()
	else:
		board = BulletinBoard.objects.filter(condition=term)[0]
	board.message_set.add(models.Message(message=message))
	c = RequestContext(request, {'purpose':'successful_feedback'})
	return HttpResponse(t.render(c))

def add_sponsor(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term').lower()
	first_name = request.POST.get('first_name')
	email = request.POST.get('email')
	buddy = Buddy(email=email, search_term=term, first_name=first_name)
	buddy.save()
	c = RequestContext(request, {})
	return HttpResponse(t.render(c))
