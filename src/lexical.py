#!/usr/bin/python3
# -*- coding : utf-8 -*-
'''
Auth: Matheus Lima
Github: github.com/matheus-lima
'''
import sys
import re
from tagger import Tagger
from word import Word
from web_scraping import WebScraping

class Lexical(object):
    def __init__(self, claim):
        self.claim = claim
        self.tagger = Tagger()
        self.web_scraping = None
        self.words = []
        self.tags_synonym = ['V', 'N', 'ADJ']
        self.tags_infinitive = ['V']

    def analyze(self):
        # Separa tokens
        _tokens = re.findall(r"[\w']+|[.,!?;]", self.claim)
        # Recupera tipo, infinitivo, sinonimos, ...
        for token in _tokens:
            word = self.__build_word(token)
            self.words.append(word)
        
    def __build_word(self, token):
        word = Word()
        tag = self.tagger.tag(token)
        word.token = token
        word.tag = tag[0][0][1]

        # Realiza querys apenas se fizer sentido.
        if word.tag in self.tags_synonym:
            word.synonyms = WebScraping(word).get_synonym()
        if word.tag in self.tags_infinitive:
            word.infinitive = WebScraping(word).get_infinitive_verb()
        print (word)
        return word

if __name__ == "__main__":
    Lexical("Eu construi o hospital de Trauma em Campina Grande").analyze()

    