import nltk

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> N | Adj N | NP PP
VP -> V NP | V N PP | Auv VP
PP -> P NP
Adj -> 'unpredictable' | 'inspiring'
N -> 'children' | 'people' | 'actions'
Auv -> 'are'
V -> 'inspiring' | 'are'
P -> 'with'
""")

sent = ['children', 'are', 'inspiring', 'people', 'with', 'unpredictable', 'actions']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)

# 1. Дети вдохновляют людей с непредсказуемым поведением
# 2. Дети вдохновляют людей своими непредсказуемыми действиями
# 3. Дети - вдохновляющие люди с непредсказуемым поведением
