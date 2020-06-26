import sys

def mkDict(lines):
    dict = {}
    for line in lines:
        tabs = line.split('\t')
        if len(tabs) == 2:
            dict[tabs[0]] = tabs[1]
    return dict

def readDict(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return mkDict(lines)


def main():
    filename = sys.argv[1]
    dict = readDict(filename)
    prompt = "ange sökord+enter, sluta med enter> "
    query = input(prompt)
    while query:
        print(dict.get(query,"hittar inte"))
        query = input(prompt)

main()



