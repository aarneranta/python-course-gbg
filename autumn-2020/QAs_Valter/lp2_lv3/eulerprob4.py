""" Find the largest palindrome made from the product of
    two 3-digit numbers. """


def is_palindrome(s):
    return s == s[::-1]


def largest_palindrome_product():
    ans = -1
    for i in range(100, 1000):
        for j in range(i, 1000):
            if is_palindrome(str(i*j)):
                if i*j > ans:
                    ans = i*j
    return ans
