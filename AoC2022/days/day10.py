from AoC2022.base.day import Day


def noop(x, clock):
    return x, clock + 1

noop.__str__ = lambda: "noop"

class addx:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, x, clock):
        return x + self.arg, clock + 2

    def __str__(self):
        return f"addx {self.arg}"


def uppermod(v, r):
    # Mod but from 1..r not 0..r-1
    t = v % r
    if t == 0:
        t = r
    return t


class Day10(Day):
    tests = ["""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""]
    part1_answers = [13140]
    part2_answers = ["""##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""]

    def parse(self):
        instructions = []
        for line in self.file.readlines():
            instruction = line.strip().split()
            if instruction[0] == "noop":
                instructions.append(noop)
            elif instruction[0] == "addx":
                instructions.append(addx(int(instruction[1])))
        return instructions

    def part1(self):
        instructions = self.parse()
        important = [20, 60, 100, 140, 180, 220]
        answer = 0
        x = 1
        clock = 1
        for instruction in instructions:
            oldx, oldclock = x, clock
            x, clock = instruction(x, clock)
            if oldclock < important[0] < clock:
                answer += oldx * important.pop(0)
            elif clock == important[0]:
                answer += x * important.pop(0)
            if len(important) == 0:
                break
        return answer

    def part2(self):
        instructions = self.parse()
        x = 1
        clock = 0
        res = ""
        for instruction in instructions:
            oldx, oldclock = x, clock
            x, clock = instruction(x, clock)
            for i in range(oldclock, clock):
                sprite = oldx
                draw = i%40

                if sprite - 1 <= draw <= sprite + 1:
                    c = "#"
                else:
                    c = "."
                res += c
        blocks = map("".join, zip(*(iter(res),) * 40))
        screen = "\n".join(blocks)
        return screen
