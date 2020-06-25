# Write a program that asks for two exam scores and averages them

def main():
    # samma som score1, score2 = 3, 7
    score1, score2, score3 = eval(input("Skriv in poängen på de tre proven med kommatecken emellan:"))
    print("Medelvärdet blir", (score1 + score2 + score3) / 3)


main()
