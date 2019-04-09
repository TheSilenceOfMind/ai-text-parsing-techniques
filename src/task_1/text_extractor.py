import re

input_filename = './ru_ar_cut.txt'
output_filename = './ru_ar_cut_parsed.txt'

fin = open(input_filename, 'rt', encoding='UTF-8-sig')
input_text = fin.read()
fin.close()

created_text = []
sentence = []
for line in input_text.split('\n'):
    if len(line) == 0:
        continue
    word = line.split('\t')[0]
    if word[0] != '<':
        sentence.append(word)
    if word == '</s>':
        created_text.append(sentence)
        sentence = []
print('parsing is done!')

normalized_text = ""
for sentence in created_text:
    out_sentence = sentence[0]
    for i in range(1, len(sentence)):
        word = sentence[i]
        previous_word = sentence[i-1]
        if re.findall("^[.,:;!?)\]}>\"»]$", word):
            out_sentence += word
        elif re.findall('^[([{<"«]$', previous_word) and word[0].isalpha():
            out_sentence += word
        else:
            out_sentence += ' ' + word
    normalized_text += out_sentence + "\n"
normalized_text = re.sub(' ¬ ', '', normalized_text)  # magical symbols (carriage return) of the words, lol
print('normalizing is done!')

out_file = open(output_filename, 'wt', encoding='UTF-8-sig')
out_file.write(normalized_text)
out_file.close()

