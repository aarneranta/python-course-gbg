import sys


# 5.4  An acronym is a word formed by taking the first letters of the words in a
#      phrase and making a word from them. For example, RAM is an acronym
#      for "random access memory." Write a program that allows the user to
#      type in a phrase and then outputs the acronym for that phrase. Note: The
#      acronym should be all uppercase, even if the words in the phrase are not
#      capitalized.
# acronym("This is a phrase") -> "TIAP"
def acronym(phrase):
    acr = []
    for word in phrase.split():
        acr.append(word[0].upper())
    return "".join(acr)
# def acronym(phrase):
#     return "".join(word[0].upper() for word in phrase.split())


# 5.10  Write a program that calculates the average word length in a sentence
#       entered by the user.
def average_word_length(sentence):
    sum_length = 0
    nr_words = 0
    for word in sentence.split():
        sum_length += len(word)
        nr_words += 1
    return sum_length/nr_words


# 5.14  Word Count. A common utility on UniX/Linux systems is a small program
#       called wc. This program analyzes a file to determine the number of
#       lines, words, and characters contained therein. Write your own version of
#       wc. The program should accept a file name as input and then print three
#       numbers showing the count of lines, words, and characters in the file.
def main():
    filename = sys.argv[1]
    nr_lines = 0
    nr_words = 0
    nr_chars = 0
    file = open(filename)
    for line in file:
        nr_lines += 1
        nr_words += len(line.split())
        nr_chars += len(line.replace(' ', '').replace('\t',
                        '').replace('\n', ''))
    print(f"Lines: {nr_lines}")
    print(f"Words: {nr_words}")
    print(f"Chars: {nr_chars}")


# 6.11 & 6.12: Write an automated censor program that reads in the text from a file and
# creates a new file where all of the four-letter words from another file have been replaced by ****
# You can ignore punctuation, and you may assume that no words
# in the file are split across multiple lines.
def parse_line(line):
    words = line.split(' ')
    for (i, word) in enumerate(words):
        if len(word) == 4:
            words[i] = '****'
    return ' '.join(words)


def main():
    input_filename = sys.argv[1]
    input_file = open(input_filename)
    output_filename = sys.argv[2]
    output_file = open(output_filename, 'w')
    for line in input_file:
        output_file.write(parse_line(line))
    input_file.close()
    output_file.close()

# main()
