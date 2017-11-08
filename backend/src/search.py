import re
import requests
from google import search
from bs4 import BeautifulSoup

URL_GOOGLE_SEARCH = 'https://www.google.com.br/search?q='
class Search(object):
    
    def __init__(self):
        self.url = ''

    def searchSnippet(self, query):
        for url in search(query, tld='com.br', lang='pt-br', stop=1):
            snippets = {}
            self.url = url
            return self.__google_scrape(query)

    def __google_scrape(self, query):
        try:
            url = URL_GOOGLE_SEARCH + query.replace(" ", "+")
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "lxml")
        except:
            return "Error 1"
        
        snippet = {}
        try:
            snippet['url'] = self.url
            snippet['phrase'] = query
            snippet['results'] = soup.find("div", {"id": "resultStats"}).text
            snippet['title'] = soup.find("h3", class_="r").find("a").text
            snippet['description'] = soup.find("span", class_="st").text
        except:
            return "Error 2"

        return snippet


if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    search_result = Search().searchSnippet(query)
    print ("Snippet: " + query)
    print ("Resultados encontrados: " + search_result['result_stats'])
    print ("Titulo: " + search_result['title'])
    print ("Descricao: " + search_result['description'])
    print ("Link: " + search_result['url'])
