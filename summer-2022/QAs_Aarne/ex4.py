# Aarne's exercise session 4, 2022-07-07
# It turned out to take more time than planned,
# and we did not finish the code for wc and invisible.
# But the final, complete code is here.
# The end part of the video is recorded again to explain this code
# not using too more time than an exercise session should last.


import sys

#### Acronym (book exercise 5.11.4) ###

# acronym in the book: first letter of every word, capitalized
def acronym(s):
    ws = s.split()
    acr = ''
    for w in ws:
        acr = acr + w[0].upper()
    return acr


# acronym English style: include only the capitalized words
def eng_acronym(s):
    ws = s.split()
    acr = ''
    for w in ws:
        if w[0].isupper():
            acr = acr + w[0]  # no need to capitalize again!
    return acr


# main function to test acronym
def acronym_main():
    s = input("ange namn: ")
    print(acronym(s))

    
# main function to test eng_acronym
def eng_acronym_main():
    s = input("ange namn: ")
    print(acronym(s))

    

### Word Count (book exercise 5.11.14) ###

# easiest possible word count
# this goes through the string s five times (each len() once)
def wc1(s):
    cs = len(s)
    ws = len(s.split())
    ls = len(s.split('\n'))
    return ls, ws, cs

# to compare with Unix wc, use 'wc -lwm'
# otherwise the count of non-ASCII characters differs
        
# a more "sophisticated" word count
# goes through s only once
# very easy to get wrong, and actually too much at this point of the course
def wc2(s):
    ls, ws, cs = 0, 0, 0
    inword = False
    for c in s:
        cs += 1
        if c.isspace():
            inword = False
            if c == '\n':
                ls += 1
        else:
            if not inword:
                ws += 1
            inword = True
    return ls, ws, cs

# you can measure the time it takes to execute a command by prefixing
# "time" to it. Surprise surprise: wc1 is faster than wc2!
# The reason is probably that the standard library functions
# len() and split() have an efficient implementation that is hard to beat
# a test run is shown at the end of this file


# main function to test wc1
def wc1_main():
   filename = sys.argv[1]
   file = open(filename, 'r')
   s = file.read()
   ls, ws, cs = wc1(s)
   print('\t'.join(['', str(ls), str(ws), str(cs), filename]))


# main function to test wc2
def wc2_main():
   filename = sys.argv[1]
   file = open(filename, 'r')
   s = file.read()
   ls, ws, cs = wc2(s)
   print('\t'.join(['', str(ls), str(ws), str(cs), filename]))



### Invisible ink, slide 4.45 ###

from invisible_ink import txt2bin, bin2txt

# create a list by alternating elements in two lists
def alternate(xs, ys):
    result = []
    last = min(len(xs), len(ys))  # to stop when one list runs out
    for i in range(last):
        result.append(xs[i])
        result.append(ys[i])
    return result


# encode mytxt in basetxt by using alternation
def txt2invisible(basetxt, mytxt):
    basewords = basetxt.split()  # convert basetxt to a list of words
    mybin = txt2bin(mytxt)  # convert mytxt to a string of 0s and 1s

    # make sure that the base text is long enough to encode your message
    if len(mybin) > len(basewords):
        print("base text too short")
        return

    # convert mybin to a list of strings consisting of one or two spaces
    spacebin = []
    for b in mybin:
        if b == '1':
            spacebin.append('  ')
        else:
            spacebin.append(' ')

    # apply alternate and join the resulting list into a string
    msg = alternate(basewords, spacebin)
    return ''.join(msg)


# develop the encrypted text myinv
# the logic resembles wc2, hence very subtle!
def invisible2txt(myinv):

    # build a list of 0s and 1s
    bin = []

    # you will be reading myinv character by character
    # at each step, inspace tells you if you are in the middle of a space
    # in the beginning there was no space of course
    inspace = False
    
    for c in myinv:
        
        if c == ' ':  # you are reading a space
            if inspace:  # the previous character was also a space
                bin.append('1')  # two spaces encode a 1
                inspace = False  # you are no longer reading a space
            else:  # the previous character was not a space
                inspace = True  # no output yet, but you have read one space
                
        else:  # you are reading a non-space character
            if inspace:  # the previous character was a space
                bin.append('0')  # there was just one of them, so it was a 0
            inspace = False  # mark that you did not read a space
            
    return bin2txt(''.join(bin))  # decode the resulting string

    
# main function to test invisible
def invisible_main():
    mytxt = open(sys.argv[2]).read()

    # when developing, no base text file is needed
    if sys.argv[1] == 'develop':
        print(invisible2txt(mytxt))
    else:
        basewords = open(sys.argv[1]).read()
        print(txt2invisible(basewords, mytxt))

        
# uncomment another one of these to test that function

# acronym_main()
# eng_acronym_main()
# wc1_main()
# wc2_main()
invisible_main()


# if running invisible_main(),
# to test encoding, send the output to a file by using the > operator:
# aarne$ python3 ex4.py data/bible.txt data/secret.txt >secret.tmp

# if you are doing this from the GitHub directory python-course-gbg/summer-2022/QAs_Aarne
# you first have to make the files in data/ available:
# aarne$ ln -s ../../data/

# to test decoding, read the file to which the output was sent:
# aarne$ python3 ex4.py develop secret.tmp


        
"""
# testing wc1_main()
aarne$ time python3 ex4.py data/bible.txt 
	100232	824192	4352286	data/bible.txt

real	0m0.139s
user	0m0.104s
sys	0m0.030s

# testing wc2_main()
aarne$ time python3 ex4.py data/bible.txt 
	100231	824192	4352286	data/bible.txt

real	0m0.443s
user	0m0.420s
sys	0m0.017s

# testing Unix wc
aarne$ time wc data/bible.txt 
  100231  824192 4452519 data/bible.txt

real	0m0.023s
user	0m0.020s
sys	0m0.003s

"""
