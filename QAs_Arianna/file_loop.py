f = open("example.txt")
lines = f.readlines()
f.close()
for line in lines:
  print(line)

# more compact
f = open("example.txt")
for line in f:
  print(line)
f.close()

# even 
with open("example.txt") as f:
  for line in f:
    print(line)