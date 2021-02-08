"""Fordon, visar exempel på arv och polymorfism."""
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def crash(self):
        print("Crash!")

    def print_max_speed(self):
        print(f"Max speed: {self.max_speed}")


class Bicycle(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)
        self.num_wheels = 2

    def make_sound(self):
        print("Pling Pling")


class Car(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed)
        self.num_wheels = 4

    def make_sound(self):
        print("Tut tut")

def main():
    l = [Bicycle(20), Car(300)]
    for vehicle in l:
        vehicle.make_sound()
        vehicle.crash()
        vehicle.print_max_speed()


"""Books/Authors, visar exempel på hur attribut kan vara objekt av en egendefinierad typ."""
class Author:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_gender(self):
        return self.gender

    def __str__(self):
        return f"Author[name={self.name}, email={self.email}, gender={self.gender}]"

class Book:
    def __init__(self, name, authors, price, qty=0):
        self.name = name
        self.authors = (authors if type(authors) == (list or tuple) else [authors])
        self.price = price
        self.qty = qty

    def get_name(self):
        return self.name

    def get_authors(self):
        return self.authors

    def get_price(self):
        return self.price

    def get_qty(self):
        return self.qty

    def set_price(self, price):
        self.price = price

    def set_price(self, qty):
        self.qty = qty

    def __str__(self):
        return f"Book[name={self.name}, authors={[str(author) for author in self.authors]}, price={self.price}, qty={self.qty}]"

main()
