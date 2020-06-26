import sys

def mkDict(lines):
    dict = {}
    for line in lines:
        tabs = line.split('\t')
        if len(tabs) == 2:
            for word in tabs[0].split(','):
                sword = word.strip()
                dict[sword] = dict.get(sword,[])
                for trans in tabs[1].split(','):
                    dict[sword].append(trans.strip())
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
        for trans in dict.get(query,["hittar inte"]):
            print(trans)
        query = input(prompt)

main()



