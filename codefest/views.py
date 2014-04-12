from django.template import loader, RequestContext
from django.http import HttpResponse
import parsers.reddit as Reddit
import parsers.healthfinder as HF
import parsers.kaiserhealthnews as KHN
import parsers.medline as ML
import parsers.pubmed as Pubmed
import parsers.autocorrect as Autocorrect
from bulletin_board.models import BulletinBoard, Message
from buddy.models import Buddy
from contact import contact_sponsor
from random import choice

def home(request, returning=False):
	t = loader.get_template('home.html')
	c = RequestContext(request, {'purpose':'home'})
	return HttpResponse(t.render(c))

def search(request):
	t = loader.get_template('results.html')
	term = request.POST.get('term').lower()
	corrected = Autocorrect.correct(term)
	reddit = Reddit.parse(term)
	healthfinder = HF.parse(term)
	kaiserhealthnews = KHN.parse(term)
	medline = ML.parse(term)
	pubmed = Pubmed.parse(term)
	sources = [healthfinder, kaiserhealthnews, medline, reddit, pubmed]
	feedback = []
	if len(BulletinBoard.objects.filter(condition=term)) != 0:
		feedback = BulletinBoard.objects.filter(condition=term)[0].message_set.all()
	no_results = 0 == sum([len(source['results']) for source in sources])
	buddies_available = len(Buddy.objects.filter(search_term=term)) > 0
	c = RequestContext(request, {'purpose':'search_results',
								 'sources': sources,
								 'no_results':no_results,
								'feedback': feedback,
								'term': term,
								'buddies': buddies_available,
								'corrected': corrected,
								 }
					   )
	return HttpResponse(t.render(c))

def submit_feedback(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term').lower()
	message = request.POST.get('message')
	if len(BulletinBoard.objects.filter(condition=term)) == 0:
		board = BulletinBoard(condition=term)
		board.save()
	else:
		board = BulletinBoard.objects.filter(condition=term)[0]
	board.message_set.add(Message(message=message))
	c = RequestContext(request, {'purpose':'successful_feedback'})
	return HttpResponse(t.render(c))

def add_sponsor(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term').lower()
	first_name = request.POST.get('first_name')
	email = request.POST.get('email')
	buddy = Buddy(email=email, search_term=term, first_name=first_name)
	buddy.save()
	c = RequestContext(request, {'purpose':'successful_buddy'})
	return HttpResponse(t.render(c))

def get_sponsor(request):
	t = loader.get_template('home.html')
	term = request.POST.get('term').lower()
	first_name = request.POST.get('first_name')
	email = request.POST.get('email')
	buddies = Buddy.objects.filter(search_term=term)
	buddy = choice(buddies.all())  # buddies[random_index]
	contact_sponsor(term,buddy.email,email,first_name)
	c = RequestContext(request, {'purpose':'successful_contact'})
	buddy.delete()
	return HttpResponse(t.render(c))
