# This program counts the amount of words entered
def main():
  sentence = input("Please write a sentence: ")
  words = sentence.split()
  print("You have written {0} words".format(len(words)))


main()
