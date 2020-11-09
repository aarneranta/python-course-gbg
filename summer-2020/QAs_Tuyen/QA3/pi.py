import math

# Check video of QA on canvas if things
# are unclear. If it still is, email us :)


def pi_approx(n):
  sum = 0
  for i in range(1, n+1):
    denominator = 2 * i - 1
    if i % 2 == 0:
      sum = sum - (4 / denominator)
    else:
      sum = sum + (4 / denominator)
  return sum


def main():
  n = int(input("Ange hur många termer som ska adderas i talserien: "))
  pi_approx_result = pi_approx(n)
  print(pi_approx_result)
  print("Skillnaden mellan Pythons pi och vår uppskattning av pi är: ",
        math.pi - pi_approx_result)


main()
