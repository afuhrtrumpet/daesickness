import requests
import xml.etree.ElementTree as ET

def correct(query):
	search_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/espell.fcgi"
	params = {'db':'pmc', 'term':query}
	api_spelling_response = requests.get(search_url, params=params)
	root = ET.fromstring(api_spelling_response.text.encode('UTF-8'))
	return root.find('CorrectedQuery').text
