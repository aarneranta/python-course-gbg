# Check video of QA on canvas if things
# are unclear. If it still is, email us :)

# (0) 1 1 2 3 5 8 13 21
def fibonacci(n):
  n1 = 0
  n2 = 1
  sum = 0
  for i in range(1, n):
    sum = n1 + n2
    n1 = n2
    n2 = sum
  return sum
