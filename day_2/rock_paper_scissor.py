ROCK_POINT = 1
PAPER_POINT = 2
SCISSOR_POINT = 3
WIN = 6
DRAW = 3
LOSE = 0

def rock(move, part_2 = False):
    if move == 'x':
        return ROCK_POINT + DRAW if not part_2 else SCISSOR_POINT + LOSE
    elif move == 'y':
        return PAPER_POINT + WIN if not part_2 else ROCK_POINT + DRAW
    elif move == 'z':
        return SCISSOR_POINT + LOSE if not part_2 else PAPER_POINT + WIN

def paper(move, part_2 = False):
    if move == 'x':
        return ROCK_POINT + LOSE if not part_2 else ROCK_POINT + LOSE
    elif move == 'y':
        return PAPER_POINT + DRAW if not part_2 else PAPER_POINT + DRAW
    elif move == 'z':
        return SCISSOR_POINT + WIN if not part_2 else SCISSOR_POINT + WIN

def scissors(move, part_2 = False):
    if move == 'x':
        return ROCK_POINT + WIN if not part_2 else PAPER_POINT + LOSE
    elif move == 'y':
        return PAPER_POINT + LOSE if not part_2 else SCISSOR_POINT + DRAW
    elif move == 'z':
        return SCISSOR_POINT + DRAW if not part_2 else ROCK_POINT + WIN

def game(opp, me, part_2 = False):
    if opp == 'a':
        return rock(me, part_2)
    elif opp == 'b':
        return paper(me, part_2)
    elif opp == 'c':
        return scissors(me, part_2)

# A for Rock, B for Paper, and C for Scissors
#part 1
# X for Rock, Y for Paper, and Z for Scissors.
#part 2
# X for lose, Y for draw, and Z for win.
with open('input.txt', 'r') as f:
    score_part_1 = 0
    score_part_2 = 0
    for line in f.readlines():
        turn = line.strip('\n').split(' ')
        opp = turn[0].lower()
        me = turn[1].lower()
        #s = game(opp, me)
        #print(opp, me, s)
        score_part_1 += game(opp, me)
        score_part_2 += game(opp, me, part_2=True)

print('Game Score part 1: ', score_part_1)
print('Game Score part 2: ', score_part_2)
