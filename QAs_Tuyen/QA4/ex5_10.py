# This program calculates the average word length in an entered sentence
def main():
  sentence = input("Please write a sentence: ")
  words = sentence.split()
  print(words)
  sum = 0
  for word in words:
    sum = sum + len(word)
  print("Your average word length in the sentence is {0:0.2f}".format(
      sum/len(words)))


# main()

# An alternative way to calculate avg word length in an entered sentence
def alt():
  sentence = input("Please write a sentence: ")
  words = sentence.split()
  letters = "".join(words)
  print("Your average word length in the sentence is {0:0.2f}".format(
      len(letters)/len(words)))


alt()
