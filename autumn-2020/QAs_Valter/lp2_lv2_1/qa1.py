def double_char(s):
    """ Ge tillbaka strängen s men upprepa alla stora bokstäver två gånger """

    return_string = ""
    for char in s:
        if char.isupper():
            return_string += char*2
        else:
            return_string += char

    return return_string


def count_sheep(n):
    for i in range(1, n+1):
        print(str(i), "sheep...", end='')


def rock_paper_scissors(hand1, hand2):
    if hand1 == "rock":
        if hand2 == "rock":
            return "Draw!"
        elif hand2 == "paper":
            return "Player 2 won!"
        elif hand2 == "scissors":
            return "Player 1 won!"
    elif hand1 == "paper":
        if hand2 == "rock":
            return "Player 1 won!"
        elif hand2 == "paper":
            return "Draw!"
        elif hand2 == "scissors":
            return "Player 2 won!"
    elif hand1 == "scissors":
        if hand2 == "rock":
            return "Player 2 won!"
        elif hand2 == "paper":
            return "Player 1 won!"
        elif hand2 == "scissors":
            return "Draw!"

# Överkurs för tillfället, smidigare lösning än ovan
def rps(p1, p2):
    beats={'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
