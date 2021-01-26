
def mean(values):
    total = 0
    for v in values:
        total = total + v
    return total/len(values)


def median(values):
    values.sort()
    size = len(values)
    mid = size//2
    if size % 2 == 1:
        return values[mid]
    else:
        return mean([values[mid-1],values[mid]])

    
def counts(items):
    dict = {}
    for it in items:
        if it in dict:
            dict[it] += 1
        else:
            dict[it] = 1
    return dict


def sort_top(dict):
    pairs = []
    for (k,v) in list(dict.items()):
        pairs.append((v,k))
    srt = sorted(pairs, reverse=True)
    return srt


def clean_text(text):
    cleaned = ""
    for char in text:
        if char.isalpha() or char.isspace():
            cleaned += char.lower()
    return cleaned


def word_freqs(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    return counts(words)


def print_word_freqs(filename,number):
    file = open(filename)
    text = file.read()
    freqs = sort_top(word_freqs(text))
    for (n,w) in freqs[:number]:
        print(w,n)
    file.close()

    
def input_numbers():
    numbers = []
    n = input("Ange ett heltal: ")
    while n != "STOP":
        numbers.append(int(n))
        n = input("Nästa heltal, STOP för avslut: ")    
    return numbers

    
def read_numbers(filename):
    file = open(filename)
    text = file.read()
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers


def read_dict(filename):
    file = open(filename) 
    dict = {}
    for line in file:
        entry = line.split()
        if len(entry) > 0:
            dict[entry[0]] = entry[1:]
    file.close()
    return dict

        
def plot_values(tuples):
    import matplotlib.pyplot as plt
    xs = []
    ys = []
    for tuple in tuples:
        if len(tuple)==2:
            xs.append(float(tuple[0]))
            ys.append(float(tuple[1]))
    plt.yscale("linear")
    plt.plot(xs,ys,'ro')
    plt.show()


    
