import matplotlib.pyplot as plt

def salary(sal,taxrate,rent):
    print("Lön",sal)
    print("Skatt",taxrate)
    tax = sal*taxrate/100
    net = sal - tax
    print("Efter skatt", net)
    print("Hyra",rent)
    print("Kvar",net - rent)

    labels = 'skatt', 'hyra', 'kvar'
    sizes = [int(tax), int(rent), int(net-rent)]
    colors = ['red','yellow','green']
    plt.pie(sizes, labels=labels, colors=colors)
    plt.show()

def growth(amount,proc,years):
    for y in range(1,years):
        amount = amount * (1 + proc/100)
        print("år",y,":",amount)

def main():
    sal = int(input("Ange bruttolön: "))
    tax = int(input("Ange skatteprocent: "))
    rent = int(input("Ange hyra: "))
    salary(sal,tax,rent)

main()




