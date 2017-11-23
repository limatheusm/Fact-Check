## Gramática original

(1) S -> NP VP 
(2) S -> VP NP 
(3) S -> VP 
(4) S -> AdvP S 
(5) NP -> det N’ 
(6) NP -> N’ 
(7) NP -> pré-det NP 
(8) N’ -> Pro51 
(9) N’ -> N 
(10) N’ -> AP N’ 
(11) N’ -> N’ AP 
(12) N’ -> N’ PP 
(13) AP -> Adj’ AdvP 
(14) AP -> Adj’ PP 
(15) AP -> AdvP Adj’ 
(16) AP -> Adj’ 
(17) Adj’ -> Adj 
(18) Adj’ -> AdvP Adj’ 
(19) Adj’ -> Adj’ AdvP 
(20) Adj’ -> Adj’ PP 
(21) PP -> P NP 
(22) PP -> P AdvP 
(23) VP -> V’ 
(24) VP -> V’ PP 
(25) VP -> AdvP V’
(26) VP -> V’ AdvP 
(27) V’ -> V’ NP 
(28) V’ -> V’ PP 
(29) V’ -> AdvP V’ 
(30) V’ -> V’ AdvP 
(31) V’ -> V 
(32) V’ -> V NP 
(33) V’ -> V PP 
(34) V’ -> V AP 
(35) V’-> V AdvP
(36) AdvP -> Adv’ 
(37) AdvP -> AdvP Adv’ 
(38) AdvP -> Adv’ PP 
(39) Adv’ -> Adv 
(40) Adv’ -> Adv’ PP 

Obs: Após retirar a recursão à esquerda na regra ADJ’, obtivemos uma recursão à esquerda 
indireta. Após a percepção do loop infinito, este erro foi corrigido e a gramática final
está logo abaixo.

## Gramática modificada

Não terminais: {S, NP, VP, ADVP, ADVP’, N’, N’’, AP, ADJ’, PP, V’, V’’, VB, ADV’}
Terminais: {art, prosub, proadj, num, pro…, n, nprop, adj, prep, v, pcp, adv}

52 regras

S -> NP VP 
S -> VP NP 
S -> VP 
S -> ADVP S 

NP -> art N’
NP -> prosub N’ 
NP -> proadj N’ 
NP -> num N’
NP -> N’ 
NP -> proadj NP 

N’ -> pro... N’’
N’ -> n N’’
N’ -> nprop N’’
N’ -> AP N’ N’’

N’’ -> AP N’’ 
N’’ -> PP N’’
N’’ -> ɛ

AP -> ADJ’ ADVP 
AP -> ADJ’ PP 
AP -> ADJ’ 
AP -> ADVP ADJ’ 

ADJ’ -> adj ADJ’’ ADJ’’’

ADJ’’ -> ADVP ADJ’’ 
ADJ’’ -> PP ADJ’’
ADJ’’ -> ɛ

ADJ’’’ -> ADVP ADJ’’ ADJ‘’’
ADJ’’’ -> ɛ

PP -> prep NP 
PP -> prep ADVP 

VP -> V’
VP -> V’ PP 
VP -> V’ ADVP
VP -> ADVP V’

V’ -> ADVP V’ V’’ 
V’ -> VB V’’
V’ -> VB NP V’’
V’ -> VB PP V’’ 
V’ -> VB AP V'’
V’ -> VB ADVP V’’

V’’ -> NP V’’  
V’’ -> PP V’’ 
V’’ -> ADVP V’’
V’’ -> ɛ

VB -> v
VB -> v pcp

ADVP -> ADV’ ADVP’
ADVP -> ADV’ PP ADVP’

ADVP’ -> ADV’ ADVP’
ADVP’ -> ɛ  

ADV’ -> adv ADV’’

ADV’’ -> PP ADV’’
ADV’’ -> ɛ

## Glossario

PREP+PRO-KS ->  PREPOSIÇÃO + PRONOME CONECTIVO SUBORDINATIVO
PCP -> PARTICÍPIO
IN -> INTERJEIÇÃO
PRO-KS -> PRONOME CONECTIVO SUBORDINATIVO
NPROP -> NOME PRÓPRIO 
PU -> PONTUAÇÃO
PROADJ -> PRONOME ADJETIVO 
NUM -> NUMERAL
PREP+PROADJ -> PREPOSIÇÃO + PRONOME ADJETIVO 
ADV -> ADVÉRBIO
ADV-KS -> ADVÉRBIO CONECTIVO SUBORDINATIVO
PREP+PROPESS -> PREPOSIÇÃO + PRONOME PESSOAL
PROSUB -> PRONOME SUBSTANTIVO
CUR -> SÍMBOLO DE MOEDA CORRENTE
PROPESS -> PRONOME PESSOAL
PREP+ADV -> PREPOSIÇÃO + ADVÉRBIO
PREP+PROSUB -> PREPOSIÇÃO + PRONOME SUBSTANTIVO
N -> NOME
V -> VERBO 
ADJ -> ADJETIVO
KC -> CONJUNÇÃO COORDENATIVA
ART -> ARTIGO (def. ou indef.)
PREP+ART -> PREPOSIÇÃO + ARTIGO
KS -> CONJUNÇÃO SUBORDINATIVA
PREP -> PREPOSIÇÃO

Adj = adjetivo 
Adv = advérbio 
AdvP = sintagma adverbial 
AP = sintagma adjetival 
Det = determinante 
DP = determiner phrase 
N = nome (ou substantivo) 
NP = sintagma nominal 
NumP = sintagma numeral 
P = preposição 
PossP = sintagma possessivo 
PP = sintagma preposicional 
QP = quantifier phrase 
S = sentença 
V = verbo 
VP = sintagma verbal 
