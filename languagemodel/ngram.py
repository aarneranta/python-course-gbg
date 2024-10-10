import sys
import random

# use your lab1 solution
from wordfreq import tokenize

# if you do not have this tokenize function, you can use
# tokenize = lambda ss: ' '.join(ss).split()

class Model:
    def __init__(self, words, n):
        """build a model from a sequence of words (or characters, or other things)
        it gives for every sequence of k<n words, the frequencies of next words
        """
        model = {}  # the model to build
        model[tuple([])] = {} # 1-gram probabilities
        context = []  # the window of the last <n words
    
        for word in words:
            # consider every final segment of the context
            ngrams = [tuple(context[-k:])
                         for k in range(min(n, len(context)))]
            ngrams.append(tuple([]))
            # increment the count of this word as the continuation of the context
            for ngram in ngrams:
                model[ngram] = model.get(ngram, {})
                model[ngram][word] = model[ngram].get(word, 0) + 1
            # move the context window by one step, appending the new word
            context.append(word)
            if len(context) > n:
                context.pop(0)
        self.model = model
        self.n = n


    def predict_next(self, prompt):
        """Generate the next word, starting from a 'prompt', 
        by a biased lottery of the previous n-1 words, using frequencies 
        encoded in the model. If there is nothing for n-1, back off to n-2, etc.
        """ 
        context = prompt[-self.n-1:]  # the last seen words, at most n-1

        # build a list of last-seen n-1-grams, starting from the longest
        ngrams = [tuple(context[-k:])
                         for k in range(min(self.n, len(context)), 0, -1)]
        ngrams.append(tuple([]))
        # go through them in descending order of length (shorter needed for back-off)
        for ngram in ngrams:
            # as soon as you find a model for an ngram...
            if ngram in self.model:
                # ... generate a random number in the range of the sum of the
                # frequencies of all possible next words
                total = sum([self.model[ngram][word] for word in self.model[ngram]])
                hit = random.randrange(total+1)
                # jump from one word to next until you hit the generated number
                for word in self.model[ngram]:
                    if hit <= self.model[ngram][word]:
                        # in that case, generate the word and stop search
                        return word
                    else:
                        # try the next word 
                        hit -= self.model[ngram][word]
                            
    def generate_text(self, prompt, limit, chars=False):
        context = prompt
        for _ in range(limit):
            word = self.predict_next(context)
            if chars:
                print(word, end='')
            else:
                print(word, end=' ')
            # update the context with the generated word
            context.append(word)
            if len(context) > self.n:
                context.pop(0)
        print()

    def print_model(self):
        for ngram in self.model:
            print(' '.join(ngram), end=' : ')
            for word in self.model[ngram]:
                print(word, self.model[ngram][word], end=', ')
            print()


def unhtml(hstring):
    "remove html tags, i.e. material between <...>"
    string=[]
    tag = False
    for c in hstring:
        if c=='<':
            tag = True
        elif c=='>':
            tag = False
        elif tag:
            continue
        else:
            string.append(c)
    return ''.join(string)


usage = "usage: ngram chars|words <ngramsize> model|<textsize> <infile> <prompt>?"
        
def main():
    if sys.argv[4:]:
        toks = sys.argv[1]
        size = int(sys.argv[2]) - 1
        mode = sys.argv[3]
        file = sys.argv[4]
        corpus = []
        ishtml = file.endswith('html')
        with open(file) as infile:
            for line in infile:
                if ishtml:
                    line = unhtml(line)
                if toks == 'chars':
                    for char in line:
                        corpus.append(char)
                else:
                    for word in tokenize([line]):
                        corpus.append(word)
        model = Model(corpus, size)
        if mode == 'model':
            model.print_model()
        elif mode.isdigit():
            prompt = sys.argv[4:]
            model.generate_text(prompt, int(mode),
                                chars=True if toks=='chars' else False)
        else:
            print(usage)
    else:
        print(usage)


if __name__ == '__main__':
    main()

            


