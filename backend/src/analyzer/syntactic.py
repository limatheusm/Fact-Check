#!/usr/bin/python3
# -*- coding:utf-8 -*-

from lexical import Lexical
from word import Word
from random import randint
from random import choice
import sys
import copy
import traceback

class Syntactic(object):
    
    def __init__(self, words):
        self.words = words
        self.index = 0
        self.snippets = []

    def analyze(self):
        try:
            return self._S()
        
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
        '''
        ToDo
            # Adicionar apenas o VP
            # Build new_snippets (arrumar: so fazer quando realmente for algum!)
        '''
        if self._NP():
            # print("Metade - {}".format(self.words[self.index].token))
            self._build_snippets(self.index)
            return self._VP()
        elif self._VP(): 
            # print("Metade - {}".format(self.words[self.index].token))
            if self.index == len(self.words) \
                or self.words[self.index].tag == "PU":
                return True
            # self._build_snippets(self.index)
            return self._NP()
        elif self._ADVP():
            return self._S()

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
    
    # Build Snippets Functions
    def _build_snippets(self, pivot_index):
        '''
        Build snippets by claim
        '''
        # Primeiro Snippet: Retorna o original
        self.snippets.append(self.__list_to_string(self.words))

        # Segundo Snippet apenas substituir por sinonimos
        self.__swap_synonyms(self.words)

        # Terceiro Snippet
        # Verifica se o pivot eh a ultima palavra, caso nao seja faz o reverso: 
        #   se tiver ponto final, a ultima palavra eh tamanho - 2
        if not (pivot_index == len(self.words) - 1 \
            or pivot_index == len(self.words) - 2 \
            and self.words[pivot_index + 1].tag == 'PU'):
            reverse_snippet = self.__reverse_snippet(pivot_index)
            # Quarto Snippet: Caso inverta, tb subistitui por sinonimos
            self.__swap_synonyms(reverse_snippet)
        print('Frases criadas: ')
        print(self.snippets)
    
    # Segundo: Trocar sinonimos
    def __swap_synonyms(self, words):
        '''
        Sorteia quantos sinonimos serao substituidos e
        sorteia qual dentre eles sera trocado
        '''
        # Copia list
        words_clone = copy.deepcopy(words)

        # Recupera indice das palavras que contem sinonimos
        synonyms_index = [index for index, word in enumerate(words_clone) if word.synonyms]

        # Randomiza quantidade de sinonimos que serao alterados. min=1
        max_range_synonyms = randint(1, len(synonyms_index))
        # Substitui sinonimos de forma aleatoria ate o limite (max_range_synonyms)
        count = 0
        while count < max_range_synonyms:
            # Gera um indice randomico dentre as word que contem sinonimos
            random_index = choice(synonyms_index)
            # Remove indice escolhido
            synonyms_index.remove(random_index)
            # Recupera uma word aleatoria
            chosen_random_word = words_clone[random_index]
            # Recupera um sinonimo aleatorio
            chosen_random_synonym = chosen_random_word.synonyms[randint(0, len(chosen_random_word.synonyms) - 1)]
            # Subistitui na list de words
            words_clone[random_index].token = chosen_random_synonym
            count += 1
        
        new_snippet = self.__list_to_string(words_clone)
        self.snippets.append(new_snippet)
        return words_clone
    
    # Terceiro: Inverter Ordem se possivel
    def __reverse_snippet(self, pivot_index):
        words = []
        for x in range(pivot_index, len(self.words)):
            words.append(self.words[x])

        for x in range(0, pivot_index):
            words.append(self.words[x])

        new_snippet = self.__list_to_string(words)
        self.snippets.append(new_snippet)
        return words

    def __list_to_string(self, words):
        '''
        Convert list to string
        '''
        return ' '.join(s.token for s in words if s.tag != 'PU')

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
