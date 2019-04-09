import re
import csv


def extract_the_text(input_filename, output_filename, pos):
    """
    Extract the text field (which number position is pos) of input_file to the separate output_file.

    :param input_filename:
    :param output_filename:
    :param pos: position of the column with text beginning with 0
    :return: nothing
    """
    out_file = open(output_filename, 'wt', encoding='UTF-8-sig')

    # there's f*cking trouble with memory!
    with open(input_filename, 'rt', encoding='UTF-8-sig') as csvfile:
        times = 0
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # pass the header
            if times == 0:
                times += 1
                continue
            out_file.write(row[pos])
            out_file.write('\n')

    out_file.close()


input_filename = '../resources/lenta-ru-news.csv'
output_filename = '../resources/lenta-ru-news_text-only.csv'
pos = 2

extract_the_text(input_filename, output_filename, pos)
