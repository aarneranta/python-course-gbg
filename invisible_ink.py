# invisible ink:
#   encrypt a file to a sequence of spaces (0) and tabs (1) by using ord()
#   develop the result by an inverse method
# example usage:
#   $ python3 invisible_ink.py encrypt binaryconv.py >f.tmp
#   $ python3 invisible_ink.py develop f.tmp

import sys
import binaryconv as bc


def padbin(bin, n):
    need = 8 - len(bin)
    bin = need*'0' + bin
    return bin


def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(padbin(bc.dec2bin(ord(c)), 8))
    return "".join(bin)


def bin2txt(bin):
    txt = []
    while bin:
        txt.append(chr(bc.bin2dec(bin[:8])))
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
    filename = sys.argv[2]
    with open(filename) as file:
        content = file.read()
    if mode == "develop":
        print(invisible2txt(content))
    else:
        print(txt2invisible(content))


if __name__ == "__main__":
     main()

     
def simpleAsciiTable():
    for a in range(0, 32):
        row = ""
        for k in range(0,8):
            row = row + str(a+32*k) + ' ' + chr(a+32*k) + '\t' 
        print(row)


