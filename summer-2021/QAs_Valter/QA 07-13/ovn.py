# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word.
# Your task is to convert strings to how they would be written by Jaden Smith.

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

from math import sqrt


def jaden_cased(string):
    acc = []
    for index, char in enumerate(string):
        if index == 0 or string[index-1].isspace():
            acc.append(char.upper())
        else:
            acc.append(char)
    return ''.join(acc)


# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
def count_repeat_chars(string):
    d = {}
    for char in string:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    count = 0
    for key, value in d.items():
        if value > 1:
            count += 1
    return count


# Väldigt svår men nyttig uppgift! DM på slack vid frågor.
# Sort the columns of a csv-file
# You get a string with the content of a csv-file. The columns are separated by commas.
# The first line contains the names of the columns.
# Write a method that sorts the columns by the names of the columns alphabetically and incasesensitive.
def sort_csv(input_filename, output_filename):
    input_file = open(input_filename)
    output_file = open(output_filename, 'w')

    # BCD,aaa,DeF,abc (utan newline i slutet)
    first_row = input_file.readline().strip()
    first_row = first_row.split(',')  # ['BCD', 'aaa', 'DeF', 'abc']

    # [('BCD', 0), ('aaa', 1), ('DeF', 2), ('abc', 3)]
    indexed_first_row = list(zip(first_row, range(len(first_row))))

    # [('aaa', 1), ('abc', 3), ('BCD', 0), ('DeF', 2)]
    sorted_indexed_first_row = sorted(
        indexed_first_row, key=lambda x: x[0].lower())

    # [1,3,0,2]
    indexes = [t[1] for t in sorted_indexed_first_row]

    input_file.seek(0)  # Läs om från början
    for line in input_file.readlines():
        curr_input_line = line.strip().split(',')

        # Här sker omordningen
        curr_output_line = ','.join(
            [curr_input_line[index] for index in indexes])

        output_file.write(curr_output_line + '\n')


sort_csv('data.csv', 'newdata.csv')
