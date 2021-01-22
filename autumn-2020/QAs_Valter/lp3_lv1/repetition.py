# %% Förslag på repetition?

# %% Exempel på objekt (klassen ej viktig, kommer senare)


class Obj:
    pass


myobj = Obj()
myobj.attribute1 = "hej"
myobj.attribute2 = 1

print(f"attribute1 is {myobj.attribute1}")

# %% Konstruktor!


class Obj:
    def __init__(self, arg):
        self.attribute1 = arg


myobj = Obj("spam")
print(f"attribute1 is {myobj.attribute1}")


# %% Metoder = klassfunktioner


class Obj:
    def __init__(self, arg):
        self.attribute1 = arg

    def print_attribute1(self):
        print(f"attribute1 is {self.attribute1}")

    def set_attribute1(self, new_value):
        self.attribute1 = new_value


myobj = Obj("hej")
myobj.print_attribute1()
myobj.change_attribute1("spam")
myobj.print_attribute1()

# Muterbarhet
# Listor är muterbara
l = [5, 3, 4]
print(l)
l[0] = 2
print(l)
# Objekt som vi själva skapar från klasser är också muterbara!

# Aliasing, Pass-by-value eller pass-by-reference

# %% Aliasing
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)

# %% Pass by value


def change_var(var):
    var = 1


x = 0
change_var(x)
print(x)

# %% Pass by reference


def change_list(lvar):
    lvar.append(1)


l = [5, 3, 4]
change_list(l)
print(l)


def does_nothing(lvar):
    lvar = [1, 2, 3]


does_nothing(l)
print(l)
