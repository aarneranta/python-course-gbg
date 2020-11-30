# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter
# words reversed
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.


def spinwords(s):
    l = []
    for word in s.split():
        if len(word) >= 5:
            l.append(word[::-1])
        else:
            l.append(word)
    return ' '.join(l)
