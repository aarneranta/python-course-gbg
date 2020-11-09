'''
A palindrome is a sentence that contains the same sequence of letters read­
ing it either forwards or backwards. A classic example is 'Able was I, ere
I saw Elba." Write a recursive function that detects whether a string is a
palindrome. The basic idea is to check that the first and last letters of the
string are the same letter; if they are, then the entire string is a palindrome
if everything between those letters is a palindrome.
'''
def isPalindrome(str):
  # remove spaces and lowercase the string
  str = (str.replace(" ", "")).lower()
  # check if the string is the same as its reverse
  return str == str[::-1]

def isPalindromeRec(str):
  if not str:
    return True
  str = (str.replace(" ", "")).lower()
  return str[0] == str[-1] and isPalindrome(str[1:-1])

'''
Write and test a recursive function max to find the largest number in a list.
The max is the larger of the first item and the max of all the other items.
'''
def maximum(list):
  # handle empty list
  if not list:
    return None
  # iteratively find max
  max = list[0]
  for el in list[1:]:
    if el > max:
      max = el
  return max

def maximumRec(list):
  # handle empty list
  if not list:
    return None
  if len(list) == 1:
    return list[0]
  return max(list[0], maximumRec(list[1:]))

'''
Write a program that solves word jumble problems. You will need a large
dictionary of English words (see previous problem). The user types in a
scrambled word, and your program generates all anagrams of the word
and then checks which (if any) are in the dictionary. The anagrams ap­pearing
in the dictionary are printed as solutions to the puzzle.
'''

def permutations(string, step = 0, perms = []):
  if step == len(string):
    perms.append("".join(string))
  for i in range(step, len(string)):
    as_list = [char for char in string]
    as_list[step], as_list[i] = as_list[i], as_list[step]
    permutations(as_list, step + 1)
  return perms


if __name__ == "__main__":
  dictpath = "/usr/share/dict/cracklib-small"
  lines = []
  with open(dictpath) as dict:
    lines = dict.readlines()
  wlist = [line[:-2] for line in lines]
  word = input("Type a (scrambled) word: ")
  for perm in permutations(word):
    if perm in wlist:
      print(perm)