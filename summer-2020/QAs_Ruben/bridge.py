# coding: utf-8

suits = '♣♦♥♠'
values = '23456789TJQKA'
valued = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

# kort från index i listorna
def card(s,v):
    return suits[s] + values[v-2]

# en kortlek
def deck():
    return [s + v for s in suits for v in values]

"""Key-funktion för att sortera i bridgeordning"""
def bridgecmp(card):
    return 13 * suits.index(card[0]) + valued[card[1]] - 2

# Man kan sortera mer effektivt genom inbygga jämförelser av värden än
# att anropa funktioner om funktionerna är dyra att anropa
def hand2tuples(cards):
    return [(suits.index(c[0]), valued[c[1]], c) for c in cards]
def tuples2hand(tuples):
    return [t[2] for t in tuples]

"""Key-funktion för att sortera pokerhänder med "sträng-kort" i listor"""
def pokerrank(hand):
    # 8. färgstege
    # 7. fyrtal
    # 6. kåk
    # 5. färg
    # 4. stege
    # 3. triss
    # 2. tvåpar
    # 1. par
    # 0. högt kort
    # Därefter rankar man efter valörerna i ingående korten i handen,
    # och till sist efter valörerna i övriga kort

    # Vi använder oss flitigt av comprehensions. Kom ihåg,
    # att skriva [f(x) for x in X] är samma som
    # out = []
    # for x in X:
    #   out.append(f(x))
    # fast på en rad.

    # valörer i siffor sorterade i fallande ordning
    values = sorted([valued[c[1]] for c in hand], reverse=True)
    # färger
    suits = [c[0] for c in hand]
    
    # vi har en stege om valörerna är lika med motsvarande följd eller är A2345
    straight = (values == list(range(values[0],values[0]-5,-1)) or values == [14, 5, 4, 3, 2])
    # vi har färg om alla kort har samma färg - all(X) är sann om alla element i X är sanna
    flush = all(s == suits[0] for s in suits)

    if straight and flush:
        return (8, values)
    if flush:
        return (5, values)
    if straight:
        return (4, values)

    # listor med vilka valörer vi har triss eller par i
    trips = []
    pairs = []
    # set(values) tar bort dubbletter (bland annat) så vi bara räknar
    # varje unik valör och testar hur många vi har av respektive
    for v in set(values):
        # vi har fyrtal direkt om vi har fyra lika
        if values.count(v) == 4:
            return (7, v, values)
        elif values.count(v) == 3:
            trips.append(v)
        elif values.count(v) == 2:
            pairs.append(v)

    # vi har kåk om vi har triss och par samtidigt
    # Kom ihåg, en lista är sann om den är icke-tom
    if trips and pairs:
        return (6, trips[0], pairs[0], values)
    elif trips:
        return (3, trips[0], values)
    elif pairs:
        return (len(pairs), tuple(sorted(pairs, reverse=True)), values)

    return (0, values)

