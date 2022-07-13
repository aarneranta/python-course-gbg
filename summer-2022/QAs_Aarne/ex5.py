# exercise session 5

import sys

# remove html tags
# simple-minded method: remove everything between < and >, inclusive
def unhtml(s):
    result = []
    intag = False
    for c in s:
        if c == '<':
            intag = True
        elif c == '>':
            intag = False
        elif intag:
            pass
        else:
            result.append(c)

    return ''.join(result)


def unhtml_main():
    filename = sys.argv[1]
    file = open(filename)
    for line in file:
        print(unhtml(line[:-1]))  # ignore the \n at the end of line
    file.close()


# read a frequency table from a file such as produced in Lab 1    
def read_freq(lines):
    dict = {}
    for line in lines:
        words = line.split()
        dict[words[0]] = int(words[1])
    return dict


# arithmetic mean of a list of numbers
def mean(numbers):
    if not numbers:
        print("cannot compute mean of an empty list")
    else:
        return sum(numbers)/len(numbers)


# median
def median(numbers):
    if not numbers:
        print("cannot compute median of an empty list")
    else:
        numbers = sorted(numbers)
        size = len(numbers)
        midpoint = size // 2
        if size % 2 == 0:  # even length of list
            return (numbers[midpoint] + numbers[midpoint - 1])/2
        else:
            return numbers[midpoint]


# hapax words: once that occur only once
def hapax(freqs):
    numbers = freqs.values()
    haps = 0
    for n in numbers:
        if n == 1:
            haps += 1
    return haps


# demo with different statistical properties from a frequency file
def stat_main():
    filename = sys.argv[1]
    file = open(filename)
    freqs = read_freq(file)
    file.close()
    
    numbers = freqs.values()

    print("antal: ", len(numbers))
    print("genomsnitt: ", mean(numbers))
    print("median: ", median(numbers))
    print("hapax ord: ", hapax(freqs))


# scalar product of two vectors given as lists of numbers
def scalar_product(A, B):
    if len(A) != len(B):
        print("Error: different lengths")
    else:
        prod = 0
        for i in range(len(A)):
            prod += A[i] * B[i]
        return prod


# Euclidian length of a vector
def vector_length(A):
    result = 0
    for n in A:
        result += n*n
    return result ** 0.5


# cosine of vectors as lists of numbers
def vector_cosine(A, B):
    return scalar_product(A, B) / (vector_length(A) * vector_length(B))


# cosine of frequency tables
# each word in the two tables is a dimension
def freq_cosine(F, G):
    
    # start with words from F
    words = list(F.keys())
    # add words from G
    for word in G:
        if word not in F:
            words.append(word)
    # now you have a list of all words in either F or G

    # create vectors for all words
    VF = []
    for word in words:
        VF.append(F.get(word, 0))
    VG = []
    for word in words:
        VG.append(G.get(word, 0))

    # compute their cosine
    return vector_cosine(VF, VG)


def main():
    FA = read_freq(open(sys.argv[1]))
    FB = read_freq(open(sys.argv[2]))
    CAB = freq_cosine(FA, FB)
    print('cosinus-likhet: ', CAB)


if __name__ == '__main__':
    main()

