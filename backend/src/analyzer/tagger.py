#!/usr/bin/python3
# -*- coding : utf-8 -*-
'''
Auth: Matheus Lima
Github: github.com/matheus-lima
'''

import nlpnet
import os

class Tagger(object):
    def __init__(self):
        self.tagger = nlpnet.POSTagger(os.path.dirname(os.path.realpath(__file__)) + "/pos-pt", language='pt')
    def tag(self, token):
        return self.tagger.tag(token)[0]