from analyzer.word import Word
from random import randint
from random import choice
import copy

class BuildSnippet(object):
    
    def __init__(self):
        self.snippets = []
    
    def __list_to_string(self, words):
        '''
        Convert list to string
        '''
        return ' '.join(s.token for s in words if s.tag != 'PU')
    
    def __swap_synonyms(self, words):
        '''
        Sorteia quantos sinonimos serao substituidos e
        sorteia qual dentre eles sera trocado
        '''
        # Copia list
        words_clone = copy.deepcopy(words)
        
        # Recupera indice das palavras que contem sinonimos
        synonyms_index = [index for index, word in enumerate(words_clone) if word.synonyms]

        if len(synonyms_index) == 0:
            return

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
        return new_snippet

    def __reverse_snippet(self, words, pivot_index):
        new_words = []
        for x in range(pivot_index, len(words)):
            new_words.append(words[x])

        for x in range(0, pivot_index):
            new_words.append(words[x])

        new_snippet = self.__list_to_string(new_words)
        self.snippets.append(new_snippet)
        return new_words

    # Build Snippets Functions
    def build(self, words, pivot_index):
        '''
        Build snippets by claim
        '''
        # Primeiro Snippet: Retorna o original
        self.snippets.append(self.__list_to_string(words))

        # Segundo Snippet apenas substituir por sinonimos
        self.snippets.append(self.__swap_synonyms(words))

        # Terceiro Snippet
        # Verifica se o pivot eh a ultima palavra, caso nao seja faz o reverso: 
        #   se tiver ponto final, a ultima palavra eh tamanho - 2
        if not (pivot_index == len(words) - 1 \
            or pivot_index == len(words) - 2 \
            and words[pivot_index + 1].tag == 'PU'):
            reverse_snippet = self.__reverse_snippet(words, pivot_index)
            # Quarto Snippet: Caso inverta, tb subistitui por sinonimos
            self.snippets.append(self.__swap_synonyms(reverse_snippet))

        return self.snippets