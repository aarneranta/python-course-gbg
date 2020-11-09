#Program written together during QA session. Not finished, but a fun little example if you want to practice using
#dictionaries and modify it to be robust to different types of input. A good start is to look at why it prints
#colors that aren't colors at all (such as numbers).

def get_colors():
    prompt = "Give me a color in your rainbow, please."
    color = input(prompt)
    colors = {}
    while color:
        for c in color:
            if not c.isalpha():
                print("Buuuh! Inte en färg!")
                color = input(prompt)

        color = color.lower()
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1

        color = input(prompt)

    return colors


def print_number_of_colors(colors):
    print(colors)

def main():
    colors = get_colors()
    print_number_of_colors(colors)


if __name__ == '__main__':
    main()
