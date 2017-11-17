#!/usr/bin/python3
# -*- coding:utf-8 -*-
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
        # Separa tokens e Recupera tipo, infinitivo, sinonimos, ...
        tokens = self.tagger.tag(self.claim)[0]
        for token in tokens:
            word = Word()
            word.token = token[0]
            word.tag = token[1]
            # Realiza querys apenas se fizer sentido.
            if word.tag in self.tags_synonym:
                word.synonyms = WebScraping(word).get_synonym()
            if word.tag in self.tags_infinitive:
                word.infinitive = WebScraping(word).get_infinitive_verb()
            self.words.append(word)
        #self.__print_list()
        return self.words
    
    def __print_list(self):
        for word in self.words:
            print(word)

if __name__ == "__main__":
    Lexical("o Rato roeu a roupa do rei de Roma").analyze()

    