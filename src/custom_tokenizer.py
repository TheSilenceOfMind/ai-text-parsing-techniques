# how do we tokenize text:
#   1. split by delimiters to the smallest particles
#   2. join context-important text to one token
#       - formulas (started with letter and has digits, other letters, dash)
#       - numbers: digits separated with commas and the measurement characteristics (celsius, pascal and so on)
#       - everything in quotes (', ")
#   3. remove commas, dots, etc.
#   4. present our set of tokens

import re

filename = './chemistry_text.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

open_braces = ['(', '[', '{', '«', '\'', '"']
close_braces = [')', ']', '}', '»', '\'', '"']
measurements_suffixes = ['°C', 'МПа', 'Дж/моль·K', 'г', 'К', 'кДж/моль']
quotes = ['\'', '"']


def join_numbers_with_measurements(input_tokens):
    output = []
    for token in input_tokens:
        # determine the number-characteristics
        if token in measurements_suffixes and re.findall('^[+-]?\d+[.,]?\d*$', output[-1]):  # match any number
            output[-1] += token
            print(output[-1])
        else:
            output.append(token)
    return output


def join_everything_in_quotes(input_tokens):
    output = []
    within_quotes = 0
    for token in input_tokens:
        if token in quotes:
            output.append(token)
            within_quotes = (within_quotes + 1) % 2
        else:
            if not within_quotes:
                output.append(token)
            else:  # are within quotes
                if output[-1] in quotes:
                    output.append(token)
                else:
                    output[-1] += ' ' + token
    return output


def join_to_context_related_tokens(input_tokens):
    """
    The function joins
        + formulas (started with letter and has digits, other letters, dash)
        + numbers: digits separated with commas and the measurement characteristics (celsius, pascal and so on)
        - everything in quotes (', ")

    :param input_tokens:
    :return: new list of "joined" tokens
    """
    output = join_everything_in_quotes(join_numbers_with_measurements(input_tokens))
    return output


def separate_braces(tokens):
    """
    The function splits the token with braces in separate tokens (braces are distinct tokens in out list)

    returns new list of tokens
    """
    out = []
    for token in tokens:
        chars = list(token)
        storage = []  # a register to store tmp word
        for c in chars:
            if c in open_braces + close_braces:  # whenever reach brace put the word
                if len(storage):
                    out.append(''.join(storage))
                    storage = []
                out.append(c)
            else:
                storage.append(c)
        if len(storage):
            out.append(''.join(storage))
    return out


# text = '"этиловый спирт"'
splitted_text = separate_braces(re.split('\s+', text))
rejoined_text = join_to_context_related_tokens(splitted_text)
print(join_everything_in_quotes(splitted_text))
