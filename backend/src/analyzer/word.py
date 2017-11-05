#!/usr/bin/python3
# -*- coding : utf-8 -*-
'''
Auth: Matheus Lima
Github: github.com/matheus-lima
'''

class Word(object):
    def __init__(self, token, tag, infinitive):
        self.token = token
        self.tag = tag
        self.infinitive = ''
        self.synonyms = []

    def __init__(self):
        self.token = ''
        self.tag = ''
        self.infinitive = ''
        self.synonyms = []

    def __repr__(self):
        return "Word: {}\nTag: {}\nInfinitive: {}\nSynonym: {}\n".format(self.token, self.tag, self.infinitive, self.synonyms)