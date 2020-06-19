# invisible ink:
#   encrypt a file to a sequence of spaces (0) and tabs (1) by using ord()
#   develop the result by an inverse method
# example usage:
#   $ python3 invisible_ink.py encrypt mathChapter3.py >f.tmp
#   $ python3 invisible_ink.py develop f.tmp

import sys
import mathChapter3 as ma

def padbin(bin,n):
    need = 8 - len(bin)
    for i in range(need):
        bin = '0' + bin
    return bin

def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(padbin(ma.dec2bin(ord(c)),8))
    return "".join(bin)

def bin2txt(bin):
    txt = []
    while bin:
        txt.append(chr(ma.bin2dec(bin[:8])))
        bin = bin[8:]
    return "".join(txt)

def bin2invisible(bin):
    inv = []
    for b in bin:
        if b=='0':
            inv.append(' ')
        else:
            inv.append('\t')
    return "".join(inv)

def invisible2bin(inv):
    bin = []
    for b in inv:
        if b==' ':
            bin.append('0')
        elif b=='\t':
            bin.append('1')
        else:
            pass
    return "".join(bin)

def txt2invisible(txt):
    return bin2invisible(txt2bin(txt))

def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))

def main():
    mode = sys.argv[1]
    file = sys.argv[2]
    src = open(file)
    content = src.read()
    if mode == "develop":
        print(invisible2txt(content))
    else:
        print(txt2invisible(content))
    src.close()

main()


    


