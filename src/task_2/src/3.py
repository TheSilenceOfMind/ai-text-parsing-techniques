import csv


def get_keywords_list(filename):
    file = open(filename, 'r', encoding='UTF-8-sig')
    res = []
    for l in file:
        res.append(' {} '.format(l.replace('\n', '')))
    file.close()
    print('Ключевые слова прочитаны')
    return res


def parse_corpus(output):
    i = 0
    for row in corpus:
        for k in keywords:
            if k in row:
                output.append(row)
        i += 1
        if i % 100 == 0:
            print('{}% корпус'.format(round(i / 1449439 * 100, 0)))
    return output


def parse_lenta(output):
    i = 0
    for row in lenta:
        # знак вопроса - непонятная дичь в конце каждого слова (см. в файл)
        data = row[3].replace('{', '').replace('?', '').replace('}', ' ')

        for k in keywords:
            if k in data:
                output.append(data)
        i += 1
        if i % 100 == 0:
            print('{}% лента'.format(round(i / 791162 * 100, 0)))
    return output


lenta_filename = '../resources/lenta-ru-news.csv.out'
corpus_filename = '../resources/russian_news.txt'
keywords_filename = '../resources/natural_disasters_keywords.txt'
output_filename = '../resources/3.out'

corpus = open(corpus_filename, 'r', encoding='ISO-8859-1')
lenta = csv.reader(open(lenta_filename, 'r', encoding='UTF-8-sig'))

# Прошерстим по каждому из документов и проверим, есть ли вхождения ключевых слов.
# Если таковые есть, добавляем в output новость.
output = []
keywords = get_keywords_list(keywords_filename)
output = parse_corpus(output)
output = parse_lenta(output)

# Записать результат в файл
i = 0
l = len(output)
out = open(output_filename, 'w', encoding='UTF-8-sig')
for s in output:
    out.write(s.replace('\n', '') + '\n')
    print('{} из {} записано'.format(i, l))
out.close()
