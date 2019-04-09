import nltk
from nltk.collocations import *
from nltk.corpus import PlaintextCorpusReader

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

f = open('/home/kamivao/Downloads/ngramsList.txt')
raw = f.read()

tokens = nltk.word_tokenize(raw,'russian',True)
#print(tokens[:10])

text = nltk.Text(tokens)
#text.collocations()

#http://www.nltk.org/_modules/nltk/collocations.html
finder_bi = BigramCollocationFinder.from_words(text)
finder_thr = TrigramCollocationFinder.from_words(text)


print(finder_bi.nbest(bigram_measures.pmi, 10))
print(finder_thr.nbest(trigram_measures.pmi, 10))

#words = gutenberg.words("burgess-busterbrown.txt")
