# Return the number (count) of vowels in the given string.


def n_vowels(s):
    sum = 0
    for char in s:
        if char in "aeiou":
            sum += 1
    return sum


# Second version
def n_vowels2(s):
    return sum([char in "aeiou" for c in s])
