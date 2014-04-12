import requests
import xml.etree.ElementTree as ET

def parse(query):
	search_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
	params = {'db':'pubmed', 'term':query}
	api_search_response = requests.get(search_url, params=params)
	root = ET.fromstring(api_search_response.text.encode('UTF-8'))
	item_ids = ""
	for id_item in root.find('IdList'):
		item_ids += id_item.text + ","
	summary_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
	params = {'db':'pubmed', 'id': item_ids}
	api_summary_response = requests.get(summary_url, params=params)
	root = ET.fromstring(api_summary_response.text.encode('UTF-8'))
	results = []
	
	for doc_sum in root.findall('DocSum'):
		result = {}
		result['url'] = "http://www.ncbi.nlm.nih.gov/pubmed/" + doc_sum.find('Id').text
		for item in doc_sum.findall('Item'):
			if item.attrib["Name"] == "Title":
				result['title'] = item.text
				results.append(result)
	pubmed_item = {'title': 'Pubmed', 'site_url': 'http://www.ncbi.nlm.nih.gov/pubmed/', 'icon_url': '/media/img/khn.gif', 'results': results}
	return pubmed_item 
