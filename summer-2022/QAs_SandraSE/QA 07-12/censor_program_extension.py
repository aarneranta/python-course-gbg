# From Chapter 11 Programming Exercise 12
#
# Extend the program from the previous exercise to accept a file of censored
# words as another input. The words in the original file that appear in the
# censored words file are replaced by a string of '*'s with length equal to
# the number of characters in the censored word.
import sys


def replace_words(text):
    words = text.split()

    for i in range(0, len(words)):
        if len(words[i]) == 4:
            words[i] = '****'

    censored_text = ' '.join(words)
    return censored_text


def censor_words(original_file, words):
    words_list = words.split()
    text_to_edit = original_file.split()

    for i in range(0, len(text_to_edit)):  # Iterating over each word in the original file.
        for j in range(0, len(words_list)):  # For each word in the original file, we compare it to the censoring words.
            if text_to_edit[i] == words_list[j]:
                text_to_edit[i] = '*' * len(words_list[j])

    censored_text = ' '.join(text_to_edit)
    return censored_text


def main():

    filename = sys.argv[1]
    file = open(filename)
    file_content = file.read()

    censored_file_content = replace_words(file_content)
    new_file = open("new_file.txt", "x")
    new_file.write(censored_file_content)
    new_file.close()

    filename_2 = sys.argv[2]
    file_2 = open(filename_2)
    file_content_2 = file_2.read()

    result = censor_words(file_content, file_content_2)
    new_file = open("new_file.txt", "a")
    new_file.write('\n' + result)
    new_file.close()


main()
