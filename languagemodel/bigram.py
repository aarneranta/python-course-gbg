import random

def build_model(tokens):
    context = ()
    model = {context: {}}
    for t in tokens:
        model[context] = model.get(context, {})
        model[context][t] = model[context].get(t, 0) + 1
        model[()][t] = model[()].get(t, 0) + 1
        context = t
    return model


def predict_next(model, context):
    alts = model.get(context, model[()])
    # generate a random number in the range of the sum of the
    # frequencies of all possible next words
    total = sum([alts[word] for word in alts])
    hit = random.randrange(total+1)
    # jump from one word to next until you hit the generated number
    for word in alts:
        if hit <= alts[word]:
            # in that case, generate the word and stop search
            return word
        else:
            # try the next word 
            hit -= alts[word]

            
with open('mini.txt') as file:
    tokens = file.read().split()
    model = build_model(tokens)
    print('MODEL:\n', model)
    print('SAMPLE:')
    context = ()
    for k in range(100):
        token = predict_next(model, context)
        print(token, end=' ')
        context = token

(): {'det': 4, 'var': 2, 'inte': 1, 'bara': 1, '.': 1}
              
