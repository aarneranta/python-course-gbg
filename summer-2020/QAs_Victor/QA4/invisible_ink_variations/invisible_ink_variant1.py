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
input: bin, book, chars_per_line
bin är en sträng av 0or och 1or som är en binär representation av det krypterade meddelandet
book är textsträngen som book.txt innehåller.
chars_per_line bestämmer hur många ' ' och '\t' karaktärer det får vara per rad
output:
En kortare version av book.txt med det hemliga meddelandet gömt som '\t' och ' ' symbolerna mellan raderna.
'''
def bin2invisible(bin,book,chars_per_line):
    #Antal rader vi behöver behålla av boken.
    lines_needed=(len(bin)//chars_per_line)+1

    # leta upp indices i bok-strängen där vi har 2st '\n' som följer efter varandra.
    # slicea denna lista och behåll enbart lines_needed stycken element.
    newline_indices=[i+1 for i in range(len(book)-1) if book[i]=='\n' and book[i+1] == '\n'][:lines_needed]

    #ta med alla karaktärer upp till sista '\n\n' sekvensen i strängen.
    inv=[book[i] for i in range(newline_indices[-1:][0]+1)]

    currline=0 # håll koll på vilken rad vi är på
    offset=0 # håll koll på vilken karaktär vi är på
    newline_index=newline_indices[currline] #nuvarande raden

    for b in bin:
        if offset % chars_per_line == 0 and offset != 0:
            currline+=1 # ny rad
            newline_index=newline_indices[currline]
        if b=='0':
            inv.insert(newline_index+offset,' ')
        else:
            inv.insert(newline_index+offset,'\t')
        offset+=1
    inv.append('\n')
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
    while i < len(inv)-1:
        if inv[i]=='\n':
            i+=1
            #isspace() kollar efter ' ', men också '\n' och '\r'.
            #i kan i detta skedet vara större än len(inv) pga att boken kan
            # sluta med en '\n' karaktär.
            while inv[i].isspace() and not i >= len(inv)-1:
                if inv[i] == ' ':
                    bin.append('0')
                elif inv[i] == '\t':
                    bin.append('1')
                i+=1
        i+=1
    return "".join(bin)

def txt2invisible(txt,book):
    return bin2invisible(txt2bin(txt),book,10)

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
