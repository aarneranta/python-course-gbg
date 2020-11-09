"""
mcmccrack.py
Usage: python3 mcmccrack.py secret.txt counts_eng_austen.txt

This material is based on an example in
Dobrow, Robert P. Introduction to stochastic processes with R. Hoboken, New Jersey: John Wiley & Sons, 2016.
If you found this interesting and would like to further explore this theory I
suggest taking MVE550 Stochastic processes and Bayesian inference at Chalmers,
which for the year 20/21 will be available as a single-subject course.

The insight behind Bayes' formula has basically created an entire subfield of
statistics --- Bayesian statistics. While this is not a mathematical course,
we can still showcase some cool applications of theory which are not that
hard to implement, even if we don't understand the details.
This is an example of a Markov chain Monte Carlo solution to crack
a substitution cipher (a cipher where each letter is mapped to some other
letter in the alphabet). The usual knowledge used to crack these codes
is frequency tables of letter pairs in the message language (here
English). However, to find the likelihood that a certain mapping was used
to encode the message would require that we calculate the internal frequencies
for EVERY such mapping (of which there are 27! ~ 10^80) which would be
intractable...

Nevertheless, a smart idea comes to the rescue; the Metropolis-Hastings
algorithm (of great fame and use in among other things physics) allows us
to avoid what is essentially the denominator in the probability expression,
by only requiring us to compare the quotient of scores between two mappings.
Thus, we can wander randomly on the network of mappings (with the edge between
two mappings changing by one permutation), but with the probability of moving
dependent on the new mapping being sufficiently "better" than the last.
"""

import sys
from string import ascii_lowercase
import random
import numpy as np

IDENTITY = ascii_lowercase + ' '

class Map():
    def __init__(self, code=IDENTITY):
        self.map = {}
        for i in range(len(code)):
            self.map[IDENTITY[i]] = code[i]
        self.inv_map = {v: k for k, v in self.map.items()}
    def get_map(self):
        return self.map
    
    def find(self, ch):
        if ch not in IDENTITY:
            ch = ' '
        return IDENTITY.find(self.map[ch])
    def _map(self, txt, m):
        out = ''
        for ch in txt:
            if ch in m:
                out += m[ch]
            else:
                out += ch
        return out
    
    def decode(self, txt):
        return self._map(txt, self.map)
    def encode(self, txt):
        return self._map(txt, self.inv_map)
    
    def swapped(self, i, j):
        code = list(self.map.values())
        code[i], code[j] = code[j], code[i]
        code = ''.join(code)
        return Map(code)
        

def score(m, txt, lcounts):
    return sum(lcounts[m.find(txt[i]), m.find(txt[i+1])] for i in range(len(txt)-1))
        

def main():
    f = open(sys.argv[1])
    message = f.read()
    print(message)
    f.close()
    counts = np.loadtxt(sys.argv[2], dtype=int)
    lcounts = np.log(counts + 1)
    
    m = Map()
    for k in range(10000):
        i,j = random.sample(range(len(IDENTITY)), 2)
        s = m.swapped(i,j)
        a = np.exp(score(s, message, lcounts) - score(m, message, lcounts))
        if random.random() < a:
            m = s
        if k % 200 == 0:
            print(k, '-', m.decode(message), '\n')
    print('**** -', m.decode(message), '\n')

if __name__ == '__main__':
    main()