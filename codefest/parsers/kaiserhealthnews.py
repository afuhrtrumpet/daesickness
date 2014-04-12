import requests
import xml.etree.ElementTree as ET

def parse(query):
	url = "http://www.kaiserhealthnews.org/Search.aspx"
	params = {'search_collection':'khn_collection', 'search_count':'20', 'search_all':query, 'rss':'1'}
	api_response = requests.get(url, params=params)
	root = ET.fromstring(api_response.text.encode('UTF-8'))
	results = []
	for topic in root.find('channel').findall('item'):
		result = {}
		result['title'] = topic.find('title').text
		result['url'] = topic.find('link').text
		results.append(result)
	kaiser_item = {'title': 'Kaiser Health News', 'site_url': 'http://www.kaiserhealthnews.org', 'icon_url': '/media/img/khn.gif', 'results': results}
	return kaiser_item
