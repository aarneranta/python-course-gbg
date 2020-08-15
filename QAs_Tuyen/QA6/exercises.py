def main():
  if 7 < 8:
    print("7 is less than 8")
  else:
    print("Hello world")

  for i in range(10):
    for j in range(10):
      print(i, j)
      if j == 2:
        exit()


main()
