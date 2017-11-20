#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import copy
import traceback
from random import randint
from random import choice
from analyzer.lexical import Lexical
from analyzer.word import Word
from analyzer.build_snippet import BuildSnippet

class Syntactic(object):
    
    def __init__(self, words):
        self.words = words
        self.index = 0
        self.snippets = []
        self.pivot_index = 0
        self.buildSnippet = BuildSnippet()

    def analyze(self):
        try:
            if self._S():
                return self.snippets
            else:
                return False
        
        except RuntimeError as re:
            if re.args[0] != 'maximum recursion depth exceeded':
                # different type of runtime error
                raise
            print('Sorry but this syntactic solver was not able to finish '
                    'analyzing the phrase: {}'.format(re.args[0]))
            return False
    
    # S = Sentenca
    def _S(self):
        # print("S'")

        if self._NP():
            # print("Metade - {}".format(self.words[self.index].token))
            self.pivot_index = self.index # Guarda Pivot
            if self._VP():
                self.snippets = self.buildSnippet.build(self.words, self.pivot_index)
                # print('Frases criadas: ')
                # print(self.snippets)
                return True
            else:
                return False
            
        elif self._VP(): 
            # Apenas VP
            if self.index == len(self.words) \
                or self.words[self.index].tag == "PU":
                return True
            # print("Metade - {}".format(self.words[self.index].token))
            self.pivot_index = self.index # Guarda Pivot
            if self._NP():
                self.snippets = self.buildSnippet.build(self.words, self.pivot_index)
                # print('Frases criadas: ')
                # print(self.snippets)
                return True
            else:
                return False

        elif self._ADVP():
            self.pivot_index = self.index # Guarda Pivot
            if self._S():
                self.snippets = self.build_snippets(self.pivot_index)
                # print('Frases criadas: ')
                # print(self.snippets)
                return True
            else:
                return False

        return False
    
    # NP = Sintagma Nominal
    def _NP(self): 
        # print("NP")
        if self.__next_word().tag in ["ART", "NUM"]:
            if self._N_():
                return True
            else:
                self.__back_word()
                return False
        else:
            self.__back_word()
        
        if self.__next_word().tag == "PROSUB":
            if self._N_():
                return True
            
            self.__back_word()
            return False
        else:
            self.__back_word()

        if self.__next_word().tag == "PROADJ":
            if self._N_() or self._NP():
                return True
            self.__back_word()
            return False
        else:
            self.__back_word()
        
        return self._N_()
    
    # N_ = N LINHA
    def _N_(self):
        # print("N'")
        if self.__next_word().tag in ["N", "NPROP"]:
            if self._N__():
                return True
            else:
                self.__back_word()
                return False
        else:
            self.__back_word()

        if "PRO" in self.__next_word().tag:
            if self._N__():
                return True
            else:
                self.__back_word()
                return False
        else:
            self.__back_word()
        
        if self._AP():
            if self._N_():
                return self._N__()
            return False
        else:
            return False
    
    # N__ = N LINHA LINHA
    def _N__(self):
        # print("N''")
        if self.__is_last_word():
            return True

        elif self._AP() or self._PP():
            return self._N__()

        return True # Aceita vazio

    # AP = Sintagma Adjetival
    def _AP(self):
        # print("AP")
        if self._ADJ_():
            if self._ADVP() or self._PP():
                return True
    
            return True # Apenas ADJ_ tambem eh aceito
        
        elif self._ADVP():
            return self._ADJ_()

        return False

    # ADJ_ = Adjetivo linha
    def _ADJ_(self):
        # print("ADJ'")
        if self.__next_word().tag == "ADJ":
            if self._ADJ__() and self._ADJ___():
                return True

            self.__back_word()
            return False
        else:
            self.__back_word()

        return False

    # ADJ__ = Adjetivo linha linha
    def _ADJ__(self):
        # print("ADJ''")
        if self.__is_last_word():
            return True
        
        elif self._ADVP() or self._PP():
            return self._ADJ__()
        
        return True # Aceita Vazio
    
    def _ADJ___(self):
        if self.__is_last_word():
            return True
        elif self._ADVP():
            if self._ADJ__():
                return self._ADJ___()
            return False
        return True

    # PP = sintagma preposicional
    def _PP(self):
        # print("PP")
        if "PREP" in self.__next_word().tag:
            
            if self._NP() or self._ADVP():
                return True

            self.__back_word()
            return False
        else:
            self.__back_word()
            return False

    # VP = Sintagma Verbal
    def _VP(self):
        # print("VP")
        if self._V_():
            if self._PP() or self._ADVP():
                pass

            return True # Aceita apenas V'

        elif self._ADVP():
            return self._V_()

        else:
            return False

    # V_ = Verbo linha
    def _V_(self):
        # print("V'")
        if self._ADVP():
            if self._V_():
                return self._V__()

            return False

        elif self._VB():
            if self._V__():
                return True

            elif self._NP() or self._PP() or self._AP() or self._ADVP():
                return self._V__()
    
            return False
        else:
            return False
    
    # V__ = verbo linha linha
    def _V__(self):
        # print("V''")
        if self.__is_last_word():
            return True
        elif self._NP() or self._PP() or self._ADVP():
            return self._V__()
    
        return True # Gera vazio

    def _VB(self):
        # print("VB")

        # if self.__next_word().tag == "V":
        #     if self.__next_word().tag == "PCP":
        #         return True
        #     else:
        #         self.__back_word()
        #     return True
        # else:
        #     self.__back_word()
        #     return False

        if self.__next_word().tag == "V":
            if self.__next_word().tag != "PCP":
                self.__back_word()
            
            return True
        else:
            self.__back_word()
            return False
    
    # ADVP = Sintagma 
    def _ADVP(self):
        # print("ADVP")
        if self._ADV_():
            if self._ADVP_():
                return True
            
            elif self._PP():
                return self._ADVP_()
            
        return False
    
    def _ADVP_(self):
        # print("ADVP'")
        if self.__is_last_word():
            return True

        if self._ADV_():
            return self._ADVP_()

        return True

    def _ADV_(self):
        # print("ADV'")
        if self.__next_word().tag == "ADV":
            if self._ADV__():
                return True
            else:
                self.__back_word()
                return False
        else:
            self.__back_word()
            return False
    
    def _ADV__(self):
        # print("ADV''")
        if self.__is_last_word():
            return True
        
        elif self._PP():
            return self._ADV__()

        return True

    # Helper
    def __next_word(self):
        if self.index < len(self.words):
            current = self.words[self.index]
            if self.index == len(self.words) - 1 and current.token in '.?!;':
                eof = Word()
                eof.tag = 'EOF'
                return eof
            
            self.index += 1
            # print("ATUAL = {} - {}".format(current.token, current.tag))
            return current
        else:   # Ultrapassou o array
            eof = Word()
            eof.tag = 'EOF'
            return eof
    
    def __back_word(self):
        self.index -= 1
        # print("BACK_ATUAL = {} - {}".format(self.words[self.index].token, self.words[self.index].tag))
        return self.words[self.index]

    def __print_stack(self):
        '''
        Show the current stack
        '''
        print("########")
        for line in traceback.format_stack():
            print(line)
        print("########")

    # Verifica se eh a ultima palavra
    def __is_last_word(self):
        if self.__next_word().tag == 'EOF': # out range
            return True
        else:
            self.__back_word()
            return False

if __name__ == "__main__":
    claim_direto = 'Cássio jogou dinheiro pela janela do predio.' # PERFEITA
    claim_indireto_vp_np = 'estudaram astronomia ontem à noite.'
    claim_indireto_vp = 'estudaram astronomia ontem.'
    wrong_claim = 'O vai aqui nao ser.'
    wrong_claim2 = 'O ir Ricardo.'

    claims = [claim_direto, claim_indireto_vp, claim_indireto_vp_np, wrong_claim, wrong_claim2]

    # for claim in claims:
    #     print("claim: {}".format(claim))
    #     print("analyzing...")
    #     print(Syntactic(claim).analyze())
    #     print()
    words = Lexical(claim_direto).analyze()
    print("Sucesso" if Syntactic(words).analyze() else "Falhou")

'''
Algumas ordens indiretas nao funcionam nesta gramatica:
Nao pode iniciar com complemento, apenas por Sintagma verbal ou nominal
'''
