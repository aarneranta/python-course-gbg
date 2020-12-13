# program kvar.py

def remains(salary,taxrate,rent):
  tax = salary * taxrate/100
  net = salary - tax
  return net - rent


def main():

  # collect input from user
  salary = int(input("Ange bruttolön: "))
  taxrate = int(input("Ange skatteprocent: "))
  rent = int(input("Ange hyra: "))

  rems = remains(salary,taxrate,rent)
  # print the result
  print("Kvar:",rems)

  if rems < 8000:
      print("För lite! Du får inget lån.")
  elif rems < 12000:
      print("På gränsen. Har du andra inkomster?")
  else:
      print("Fint! Du får lånet.")

main()
