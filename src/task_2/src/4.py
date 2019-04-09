import nltk.corpus

filename = '../resources/3.out'
output_filename = '../resources/4.out'

total_lines = sum(1 for line in open(filename, 'r', encoding='UTF-8-sig'))

f = open(filename, 'r', encoding='UTF-8-sig')
out = open(output_filename, 'w', encoding='UTF-8-sig')

i = 0
for line in f:
    data = line.split(' ')

    l = []
    for word in data:
        if not word in nltk.corpus.stopwords.words('russian'):
            l.append(word)

    out.write(' '.join(l) + '\n')
    i += 1
    print('{} из {}'.format(i, total_lines))
