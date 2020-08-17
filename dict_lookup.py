import sys

def mkDict(lines,src,tgt):
    dict = {}
    for line in lines:
        fields = line.split(';')
        if len(fields) >= 2:
            for word in fields[src].split(','):
                sword = word.strip()
                dict[sword] = dict.get(sword,[])
                for trans in fields[tgt].split(','):
                    dict[sword].append(trans.strip())
        elif fields:
            pass # print("INTE MED", line)
        else:
            pass
    return dict

def readDict(filename,src,tgt):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return mkDict(lines,src,tgt)


def main():

    if len(sys.argv) > 2:
        filename = sys.argv[1]
        src,tgt = sys.argv[2].split(',')
        dict = readDict(filename,int(src),int(tgt))
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        dict = readDict(filename,0,1)
    else:
        print("dictionary lookup from ;-separated files")
        print("usage: dict_lookup <dictfile.csv> <from_column,to_column>?")
        return
    prompt = "ange sökord+enter, sluta med enter> "
    query = input(prompt)
    while query:
        for trans in dict.get(query,["hittar inte"]):
            print(trans)
        query = input(prompt)

if __name__ == "__main__":
    main()


##############

# make a lemmatization lexicon produced from lists lemma,form,...form

def mkLemmaDict(lines):
    dict = {}
    for line in lines:
        words = line.split(',')
        lemma = words[0].strip()
        for word in words[1:]:
            sword = word.strip()
            if sword not in dict:
                dict[sword] = [lemma]
            elif lemma not in dict[sword]:
                dict[sword].append(lemma)
            else:
                pass
    return dict


