#!/usr/bin/env python3

# предназначен для формирования новой csv с text_lemmas. (см.п.1 задания)

import csv
import sys
import subprocess
from multiprocessing import Pool

file_in = open(sys.argv[1], "r")
reader = csv.reader(file_in)

file_out = open("{}.out".format(sys.argv[1]), "w")
writer = csv.DictWriter(file_out, ['url', 'title', 'text', 'text_lemmas', 'topic', 'tags'])
writer.writeheader()

text = []

def generate(row):
    proc = subprocess.Popen(['mystem', '-l', '-d'], 
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE)
    out, err = proc.communicate(row[2].encode())
    return {
        "url": row[0],
        "title": row[1],
        "text": row[2],
        "text_lemmas": out.decode(),
        "topic": row[3],
        "tags": row[4]
    }

i = 0
for row in reader:
    i += 1
    if i == 1:
        continue
    text.append(row)
file_in.close()
print("Чтение завершено")

pool = Pool(processes=80)
result = pool.map(generate, text)
pool.close()

print("Обработка завершена")

for row in result:
    writer.writerow(row)
