# a very simple dictionary builder and lookup loop
import sys

def mkDict(lines):
    dict = {}
    for line in lines:
        fields = line.split(';')
        if len(fields) >= 2:
            dict[fields[0].strip()] = fields[1].strip()
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



