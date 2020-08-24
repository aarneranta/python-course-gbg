def rowformat(row, n):
  formatted = ""
  for el in row:
    formatted += str(el) + (n - len(str(el)) + 1) * " "
  return formatted

def matprint(m):
  # flatten the list: [[1,2], [3,4]] -> [21,2,3,4] ([el for row in m for el in row])
  # replace the numbers their number of digits: [2,1,1,1]
  # get the max: 2
  longest = max([len(str(el)) for row in m for el in row])
  for row in m:
    print(rowformat(row, longest))