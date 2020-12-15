import time


def greeter():
    name = input("What is your name? ")

    while True:
        try:
            print("Hello!", name)
            time.sleep(1)
        except KeyboardInterrupt:
            name = input("What is your name? ")
        finally:
            print("Ok, let's go again!")
            time.sleep(0.5)


if __name__ == "__main__":
    greeter()
