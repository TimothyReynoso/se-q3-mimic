#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Timothy K Reynoso with help from JT and John"


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"], => ["am"]
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    with open(filename, 'r') as file:
        all_lines = file.read()
        # new_word_list = list(filter(None,all_lines.split()))
        new_word_list = all_lines.split()
        new_dict = {}
        new_dict[""] = [new_word_list[0]]
        for word in range(1, len(new_word_list)):
            if new_word_list[word - 1] in new_dict:
                # new_dict[new_word_list[word - 1]] += [new_word_list[word]]
                new_dict[new_word_list[word - 1]].append(new_word_list[word])
            else:
                new_dict[new_word_list[word - 1]] = [new_word_list[word]]
        # for i, word in enumerate((new_word_list), start=-1):
        #     if word in new_dict:
        #         new_dict[word] += [new_word_list[i + 1]]
        #     else:
        #         new_dict[word] = [new_word_list[i + 1]]
    print(new_dict)
    return new_dict


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    # +++your code here+++
    i = 0
    result = ''
    start_word = ''
    while i < num_words:
        if start_word in mimic_dict:
            random_word = random.choice(mimic_dict[start_word])
            result += (" " + random_word + " ")
            start_word = random_word
            i += 1
        else:
            start_word = ''
            i += 1
    print(result)
    return result


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
