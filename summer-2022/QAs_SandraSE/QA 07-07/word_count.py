# Chapter 5 Programming Exercise 14
#
# Word Count. A common utility on UniX/Linux systems is a small program called "wc."
# This program analyzes a file to determine the number of lines, words, and characters contained therein.
# Write your own version of wc. The program should accept a file name as input and then print three
# numbers showing the count of lines, words, and characters in the file.

import sys
# NOTE: You need to run this program from the Terminal (with the name of the file you want to read)
# > word_count.py word_count_file (or some other file)

def main():
    filename = sys.argv[1]

    file = open(filename)
    file_content = file.read()

    list_of_lines = file_content.split('\n')
    number_of_lines = len(list_of_lines)

    list_of_words = file_content.split()
    number_of_words = len(list_of_words)

    list_of_chars = list(file_content)
    number_of_chars = len(list_of_chars)

    print('Number of lines:', number_of_lines, '\nNumber of words:', number_of_words, '\nNumber of chars:',
          number_of_chars)

    input()  # This is here just to make the program window stay open once the code has run (so we can see the results)


main()
