'''
This module acts as a simple wrapper to the MedlinePlus API.

Author: William Osler <william@oslers.us>
'''

import requests
import xml.etree.ElementTree as ET # ET Go Home
from bs4 import BeautifulSoup as BS # It's actually a very nice lib thank you

searchURL = 'http://wsearch.nlm.nih.gov/ws/query'

"""
Does a search of the MedlinePlus database, finding results that contain any of
the given terms. Returns false if no result or there was an error fetching the
request. terms is a space delimited string.
"""
def parse(terms):
    results = [];
    termstr = ""
    for term in terms.split(" "):
        termstr += term + " OR "
    termstr = termstr[0:-4]
    query = {'db': 'healthTopics', 'term': termstr}

    response = requests.get(searchURL, params=query)
    if response.ok:
        tree = ET.fromstring(response.text.encode('utf-8'))
        for source in tree.findall("./list/document"):
            try:
                title = source.find("./content[@name='title']").text
                # Some titles have <span>s in them. Bad API devs, bad!
                soup = BS(title);
                for span in soup.find_all("span"):
                    span.unwrap()
                title = soup.text

                results.append({'url': source.attrib['url'], 'title': title})

            except Exception:
                pass

        return {'title': 'Medline Plus',
                'site_url': 'http://www.nlm.nih.gov/medlineplus/',
                'icon_url': '/media/img/ml.png', 'results': results}

    else:
        return False
