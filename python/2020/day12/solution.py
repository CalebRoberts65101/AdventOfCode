
with open('python\\2020\day12\data.txt') as f:
    lines = f.readlines()


# set up initial ship stuff
class Ship:
    x = 0
    y = 0
    facing = 'E'

    def __str__(self):
        return str(self.x) + ',' + str(self.y) + ':' + self.facing

minnow = Ship()

def turnShip(ship, turn):
    left_turns = ['E', 'N', 'W', 'S']
    right_turns = ['E', 'S', 'W', 'N']
    turns = []
    if turn[0] == 'L':
        turns = left_turns
    elif turn[0] == 'R':
        turns = right_turns
    else:
        print('issue with turn')
        print(turn)
        turns = None
    if turn[1] == '9': # 90 -> 1 turn
        ship.facing = turns[(turns.index(ship.facing) + 1)%4]
    elif turn[1] == '1': # 180 -> 2 turn
        ship.facing = turns[(turns.index(ship.facing) + 2)%4]
    elif turn[1] == '2': # 270 -> 3 turn
        ship.facing = turns[(turns.index(ship.facing) + 3)%4]
    else:
        print(turn)
        ship.facing = None

def moveShip(ship, update):
    f = None
    if update[0] == 'F':
        f = ship.facing
    else:
        f = update[0]
    dx = 0
    dy = 0
    if f == 'N':
        dy = 1
    elif f == 'S':
        dy = -1
    elif f == 'E':
        dx = 1
    elif f == 'W':
        dx = -1
    else:
        print('issue with move')
        print(update)
        print(ship)
        ship = None
    number = int(update[1:])
    ship.x += number * dx
    ship.y += number * dy

def updateShip(ship, update):
    if update[0] == 'L' or update[0] == 'R':
        turnShip(ship, update)
    else:
        moveShip(ship, update)

# for each instruction
for line in lines:
    updateShip(minnow, line)

print(minnow)
print(abs(minnow.x) + abs(minnow.y))