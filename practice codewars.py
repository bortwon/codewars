# Beginner Series #3 Sum of Numbers
#
#
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including
# them and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!

def get_sum(a,b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    list = [i for i in range(int(a), int(b) + 1)]
    list.sort()
    counter = 0
    for i in list:
        counter += i
    return counter


# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
#
# Examples(Input1, Input2 --> Output):
#
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"


def rps(p1, p2):
    s = 'scissors'
    p = 'paper'
    r = 'rock'
    draw = 'Draw!'
    p1_w = 'Player 1 won!'
    p2_w = 'Player 2 won!'
    if p1 == s:
        if p2 == s:
            return draw
        elif p2 == p:
            return p1_w
        else:
            return p2_w
    if p1 == p:
        if p2 == p:
            return draw
        elif p2 == r:
            return p1_w
        else:
            return p2_w
    if p1 == r:
        if p2 == r:
            return draw
        elif p2 == s:
            return p1_w
        else:
            return p2_w

    if p2 == s:
        if p1 == s:
            return draw
        elif p1 == p:
            return p2_w
        else:
            return p1_w
    if p2 == p:
        if p1 == p:
            return draw
        elif p1 == r:
            return p2_w
        else:
            return p1_w
    if p2 == r:
        if p1 == r:
            return draw
        elif p1 == s:
            return p2_w
        else:
            return p1_w