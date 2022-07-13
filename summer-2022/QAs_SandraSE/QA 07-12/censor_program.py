# From Chapter 11 Programming Exercise 11
#
# Write an automated censor program that reads in the text from a file and
# creates a new file where all of the four-letter words have been replaced by '****'•
# You can ignore punctuation, and you may assume that no words in the file are split across multiple lines.
import sys


def replace_words(text):
    words = text.split()

    for i in range(0, len(words)):
        if len(words[i]) == 4:
            words[i] = '****'

    censored_text = ' '.join(words)
    return censored_text


def main():

    filename = sys.argv[1]
    file = open(filename)
    file_content = file.read()

    censored_file_content = replace_words(file_content)
    new_file = open("new_file.txt", "x")
    new_file.write(censored_file_content)
    new_file.close()


main()
