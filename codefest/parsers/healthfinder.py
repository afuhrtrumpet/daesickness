import requests
import codefest.keys as keys
import xml.etree.ElementTree as ET
import HTMLParser

def parse(query):
	url = "http://healthfinder.gov/developers/Search.xml"
	params = {'api_key':keys.HEALTHFINDER, 'keyword':query}
	api_response = requests.get(url, params=params)
	root = ET.fromstring(api_response.text)
	results = []
	for topic in root.find('Topics').findall('Topic'):
		result = {}
                h = HTMLParser.HTMLParser()
		result['title'] = h.unescape(topic.find('Title').text)
		result['url'] = topic.find('AccessibleVersion').text
		results.append(result)
	healthfinder_item = {'title': 'Healthfinder', 'site_url': 'http://www.healthfinder.gov', 'icon_url': '/media/img/hf-apple.png', 'results': results}
	return healthfinder_item
