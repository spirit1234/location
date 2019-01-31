# -*- coding:utf-8 -*-
try:
    print(1 / 0)
except ZeroDivisionError:
    print('You can\'t divide by zero!')


def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file_obj:
            content = file_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        words = content.split()
        new_words = len(words)
        print('The file have ' + str(new_words) + ' words')


filename = ['jjq.txt', 'story.txt']
for nu in filename:
    count_words(nu)

