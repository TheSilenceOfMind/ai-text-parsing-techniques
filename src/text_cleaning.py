import nltk
import sys

print(sys.getdefaultencoding())

# чтение файла
filename = './vanilla_tokenizer_mistakes.txt'
file = open(filename, 'rt')
text = file.read()
# print(text)
file.close()

# print('Привет, мир').encode('866')

# токенизация
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
#выводим все словоупотребления в тексте:
print(tokens)

# удаляются все словоупотребления, не относящиеся к символам алфавита, в т.ч. цифры
words_literals = [word for word in tokens if word.isalpha()]
print(words_literals)

#TODO: удалить знаки пунктуации из текста