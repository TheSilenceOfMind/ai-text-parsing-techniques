import csv
import hashlib

input_filename = 'resources/24.csv'
filename = 'resources/29.csv'

# read our dataset
f = []  # stands for "file"
with open(filename, encoding='UTF-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        row.append('')
        row.append('')
        f.append(row)

# read others dataset
g = []  # stands for "given"
with open(input_filename, encoding='UTF-8-sig') as other_file:
    reader = csv.reader(other_file)
    for row in reader:
        row.append('')
        row.append('')
        g.append(row)


# array of hashes to indicate if the phrase was in use already
in_use = []
for row in f:
    needs_for_update = row[10]
    if needs_for_update != '':
        continue

    original = row[7]
    generated = row[9]
    for other_row in g:
        g_original = other_row[7]
        g_generated = other_row[9]
        hs = hashlib.sha1((g_original + g_generated).encode('utf-8'))
        if original == g_original:
            if generated == g_generated:
                if hs not in in_use:
                    in_use.append(hs)
                    row[10] = other_row[10]
                    row[11] = other_row[11]
                else:
                    continue
            # else:
            #     if hs not in in_use:
            #         in_use.append(hs)
            #         row[10] = other_row[10]
            #         row[11] = other_row[11]
            #     else:
            #         continue

new_filename = 'resources/29.gen_new.csv'

with open(new_filename, 'w+', newline='', encoding='UTF-8-sig') as new_file:
    writer = csv.writer(new_file)
    for row in f:
        writer.writerow(row)
