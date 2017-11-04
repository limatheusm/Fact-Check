#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from word import Word
from bs4 import BeautifulSoup

REGEX_VERB = re.compile(r'.* vem do verbo (.*)\. .*')

class WebScraping:

    def __init__(self, word):
        self.url = 'https://www.dicio.com.br/'
        self.soup = None
        self.word = word
        self.__initialize()
    
    def __initialize(self):
        try:
            r = requests.get(self.url + self.word.token)
            self.soup = BeautifulSoup(r.text, "lxml")
        except:
            return self.word

    def get_infinitive_verb(self):

        infinitive = ""
        
        try:
            text = self.soup.find("p", class_="significado intro-conjugacao").find("span").text
        except:
            return

        if text:
            rx_verb = REGEX_VERB.findall(text)
            if rx_verb:
                infinitive = rx_verb[0]

        return infinitive

    def get_synonym(self):
        synonym = []
        try:
            synonyms = self.soup.find("p", class_="adicional sinonimos").find_all("a")

            for word in synonyms:
                synonym.append(word.text)
        except AttributeError:
            return []

        return synonym