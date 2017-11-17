#!/usr/bin/python3
# -*- coding:utf-8 -*-

from lexical import Lexical
from word import Word
import sys
import traceback

class Syntactic(object):
    
    def __init__(self, words):
        self.words = words
        self.index = 0

    def analyze(self):
        
        if self._S():
            return True
        else:
            print("Erro na formacao da frase, burro!")
            return False
    
    # S = Sentenca
    def _S(self):
        # print("S'")
        if self._NP():
            return self._VP()
        elif self._VP():
            print(self.words[self.index].token)
            return self._NP()
        elif self._ADVP():
            return self._S()
    
    # NP = Sintagma Nominal
    def _NP(self): 
        # print("NP")

        aux = self.__next_word()
        if aux.tag in ["ART", "NUM"]:
            if self._N_():
                return True
            else:
                self.__back_word()
                return False

        elif aux.tag == "PROADJ":
            if self._N_():
                return True
            elif self._NP():
                return True
            else:
                self.__back_word()
                return False
        
        elif aux.tag == "PROSUB":
            if self._N_():
                return True
            else:
                self.__back_word()
                return False
        
        else:
            self.__back_word()
            return self._N_()
    
    # N_ = N LINHA
    def _N_(self):
        # print("N'")

        aux = self.__next_word()
        if aux.tag in ["N", "NPROP"]:
            if self._N__():
                return True
            else:
                self.__back_word()
                return False
        elif "PRO" in aux.tag:
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
        if self.is_last_word():
            return True
        elif self._AP():
            return self._N__()
        elif self._PP():
            return self._N__()
        return True # Aceita vazio

    # AP = Sintagma Adjetival
    def _AP(self):
        # print("AP")
        if self._ADJ_():
            if self._ADVP():
                return True
            elif self._PP():
                return True
            return True # Apenas ADJ_ tambem eh aceito
        elif self._ADVP():
            return self._ADJ_()

        return False

    # ADJ_ = Adjetivo linha
    def _ADJ_(self):
        # print("ADJ'")
        if self.__next_word().tag == "ADJ":
            
            if self._ADJ__():
                return True

            self.__back_word()
            return False
        else:
            self.__back_word()

        if self._ADVP():
            if self._ADJ_():
                return self._ADJ__()
            return False
        return False

    # ADJ__ = Adjetivo linha linha
    def _ADJ__(self):
        # print("ADJ''")
        if self.is_last_word():
            return True
        
        if self._ADVP():
            return self._ADJ__()
        
        elif self._PP():
            return self._ADJ__()
        
        return True # Aceita Vazio

    # PP = sintagma preposicional
    def _PP(self):
        # print("PP")
        if "PREP" in self.__next_word().tag:
            
            if self._NP():
                return True
            elif self._ADVP():
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
            
            if self._PP():
                return True

            elif self._ADVP():
                return True

            return True # Aceita apenas V'

        elif self._ADVP():
            if self._V_():
                return True
            return False

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

            elif self._NP():
                if self._V__():
                    return True
                return False
            
            elif self._PP():
                if self._V__():
                    return True
                return False
            
            elif self._AP():
                if self._V__():
                    return True
                return False
            
            elif self._ADVP():
                if self._V__():
                    return True
                return False

            return False
        
        else:
            return False
    
    # V__ = verbo linha linha
    def _V__(self):
        # print("V''")
        if self.is_last_word():
            return True
        elif self._NP():
            return self._V__()
        elif self._PP():
            return self._V__()
        elif self._ADVP():
            return self._V__()
        return True # Gera vazio

    def _VB(self):
        # print("VB")

        if self.__next_word().tag == "V":
            if self.__next_word().tag == "PCP":
                return True
            else:
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

        else:
            return False
    
    def _ADVP_(self):
        # print("ADVP'")
        if self.is_last_word():
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
        if self.is_last_word():
            return True
        
        if self._PP():
            return self._ADV__()

        return True

    # Helper 0 1 2
    def __next_word(self):
        if self.index < len(self.words):
            current = self.words[self.index]
            # self.index += 1

            if self.index == len(self.words) - 1 and current.token in '.?!;':
                eof = Word()
                eof.tag = 'EOF'
                return eof
            
            self.index += 1
            # print("ATUAL = {} - {}".format(current.token, current.tag))
            return current
        # Ultrapassou o array
        else:
            eof = Word()
            eof.tag = 'EOF'
            return eof
    
    def __back_word(self):
        self.index -= 1
        print("BACK_ATUAL = {} - {}".format(self.words[self.index].token, self.words[self.index].tag))
        return self.words[self.index]

    def __print_stack(self):
        print("########")
        for line in traceback.format_stack():
            print(line)
        print("########")

    # Verifica se eh a ultima palavra
    def is_last_word(self):
        if self.__next_word().tag == 'EOF': # out range
            return True
        else:
            self.__back_word()
            return False

if __name__ == "__main__":
    claim = 'Lucas perdeu os sapatos ontem na escola.'
    # claim_virgula = 'Ricardo, pai de lucas, foi ao supermercado.'
    claim_indireto_vp_np = 'estudaram astronomia ontem à noite os alunos.'
    claim_indireto_vp = 'estudaram astronomia.'
    wrong_claim = 'O vai aqui nao ser.'
    wrong_claim2 = 'O ir Ricardo.'
    words = Lexical(claim_indireto_vp_np).analyze()
    if Syntactic(words).analyze():
        print("Sucesso")
    else:
        print("Falhou")


'''
Algumas ordens indiretas nao funcionam, nesta gramatica nao funciona:
Nao pode iniciar com complemento, apenas por Sintagma verbal ou nominal
'''
