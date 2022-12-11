from AoC2022.base.day import Day


def move(pos, direction):
    if direction == 'L':
        return pos[0], pos[1] - 1
    elif direction == 'R':
        return pos[0], pos[1] + 1
    elif direction == 'U':
        return pos[0] - 1, pos[1]
    elif direction == 'D':
        return pos[0] + 1, pos[1]

def sgn(i):
    if i ==0:
        return i
    elif i < 0:
        return -1
    else:
        return 1

def trail(lead, tail):
    if (abs(tail[0] - lead[0]) <= 1) and (abs(tail[1] - lead[1]) <= 1):
        return tail
    leadx, leady = lead
    tailx, taily = tail

    resx = tailx + sgn(leadx - tailx)
    resy = taily + sgn(leady - taily)
    return resx, resy

class Day9(Day):
    tests = ["""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""", """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""]
    part1_answers = [13]
    part2_answers = [1,36]

    def parse(self):
        return [(lambda x: (x[0], int(x[1])))(s.strip().split()) for s in self.file.readlines()]

    def part1(self):
        locs = {(0, 0)}
        moves = self.parse()
        head = (0, 0)
        tail = (0, 0)
        for direction, steps in moves:
            for step in range(steps):
                head = move(head, direction)
                tail = trail(head, tail)
                locs.add(tail)
        return len(locs)

    def part2(self):
        locs = {(0, 0)}
        moves = self.parse()
        knots = [(0, 0)]*10
        for direction, steps in moves:
            for step in range(steps):
                knots[0] = move(knots[0], direction)
                for knot in range(9):
                    knots[knot+1] = trail(knots[knot], knots[knot+1])
                locs.add(knots[9])
        return len(locs)
