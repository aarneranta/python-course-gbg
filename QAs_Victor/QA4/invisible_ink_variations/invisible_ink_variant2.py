# -*- coding: utf-8 -*-
# invisible ink:
#   encrypt a file to a sequence of spaces (0) and tabs (1) by using ord()
#   develop the result by an inverse method
# example usage:
#   $ python3 invisible_ink.py encrypt binaryconv.py >f.tmp
#   $ python3 invisible_ink.py develop f.tmp
'''
modifierad av:
gusjarlvi@student.gu.se
'''
import sys
import binaryconv as bc

def padbin(bin,n):
    need = n - len(bin)
    bin = (need*'0' + bin)[:n]
    return bin

def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(padbin(bc.dec2bin(ord(c)),8))
    return "".join(bin)

def bin2txt(bin):
    txt = []
    while bin:
        txt.append(chr(bc.bin2dec(bin[:8])))
        bin = bin[8:]
    return "".join(txt)


'''
input: bin, book
bin är en sträng av 0or och 1or som är en binär representation av det krypterade meddelandet
book är textsträngen som book.txt innehåller.
output:
En kortare version av book.txt med det hemliga meddelandet gömt i ' ' och '  ' symbolerna.
'''
def bin2invisible(bin,book):
     # Alla index där det finns ett space i boken, slicea så att listan blir så stor som det finns bits i vår krypterade text
    space_indices=[i for i in range(len(book)) if book[i]==' '][:len(bin)]
    # Bygg en lista av karaktärer som innehåller alla bokens karaktärer upp till sista spacet vi behöver
    inv=[book[i] for i in range(space_indices[-1:][0])]
    next=0 #index för space_indices
    offs=1 #offset för att "synka" space_indices och inv.
    for b in bin:
        if b == '1':
            inv.insert(space_indices[next]+offs,' ')
            offs+=1 # Vi lade till ett till space, alltså måste vi ha ett offset för nästa gång vi lägger till ' ' i inv.
        next+=1 # Inkrementera next
    inv.append(' ') # Lägg till space på slutet av strängen
    return "".join(inv)
'''
input: inv
inv är versionen av boken som har det dolda meddelandet gömt i sig.
output:
En binär representation av det dolda meddelandet
'''
def invisible2bin(inv):
    bin = []
    i=0
    while i < len(inv):
        if inv[i]==' ':
            if inv[i+1] != ' ':
                bin.append('0')
            else:
                i+=1
                while inv[i] == ' ':
                    i+=1
                bin.append('1')
        i+=1
    return "".join(bin)

def txt2invisible(txt,book):
    return bin2invisible(txt2bin(txt),book)

def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))

def main():
    mode = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename,encoding='utf-8')
    book = open("book.txt",encoding='utf-8') ## bok "Portland, Oregon, A.D. 1999 and other sketches by J. W. Hayes" fråm gutenberg.org
    book_content = book.read()
    content = file.read()
    if mode == "develop":
        print(invisible2txt(content))
    else:
        print(txt2invisible(content,book_content))
    file.close()
    book.close()

main()

def simpleAsciiTable():
    for a in range(0,32):
        row = ""
        for k in range(0,8):
            row = row + str(a+32*k) + ' ' + chr(a+32*k) + '\t'
        print(row)
