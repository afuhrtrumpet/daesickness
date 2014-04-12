import requests
import keys
import xml.etree.ElementTree as ET

def parse(query):
	url = "http://healthfinder.gov/developers/Search.xml"
	params = {'api_key':keys.HEALTHFINDER, 'keyword':query}
	api_response = requests.get(url, params)
	root = ET.fromstring(api_response)
	results = []
	for topic in root[0].findall('topic'):
		result = {}
		result['title'] = topic.find('Title')
		result['url'] = topic.find('AccessibleVersion')
		results.append(result)
	healthfinder_item = {'site_url': 'reddit.com', 'icon_url': '', sources: results}
	return healthfinder_item
