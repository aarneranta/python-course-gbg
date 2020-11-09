# chemparse.py
# Hjälpfunktion för att läsa in molekylformler
#  för att testa lösningen till 3.7.3
#  (mao vi skrev inte koden utan testade med den)
# Efter föreläsning 4,5 är den kanske mer begriplig.

# Döljer komplexiteten i uppgiften:
def inputCHO(prompt):
    mol = chemparse(input(prompt))
    return mol['C'], mol['H'], mol['O']

# Den faktiska funktionen som kräver dicts
# och strängmanipulation (än så länge överkurs)
def chemparse(formula):
    counts = {}
    sym = ""
    num = ""
    for i in formula:
        if i.isalpha():
            if i.isupper() and sym:
                _update_count(counts, sym, num)
                sym = ""
                num = ""
            sym += i
        else:
            num += i
    # Observera att vi måste även hantera sista symbolen
    if sym:
        _update_count(counts, sym, num)
    return counts

# DRY: Don't Repeat Yourself
def _update_count(counts, sym, num):
    if len(num) == 0:
        num = 1
    else:
        num = int(num)
    sym = sym.title()
    counts[sym] = counts.get(sym, 0) + num
 
