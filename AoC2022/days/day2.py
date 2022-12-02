from enum import IntEnum

from AoC2022.base.day import Day

class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Result(IntEnum):
    Loss = 0
    Draw = 3
    Victory = 6

def uppermod(v, r):
    # Mod but from 1..r not 0..r-1
    t = v % r
    if t == 0:
        t = r
    return t

class Day2(Day):
    tests = ["""A Y
B X
C Z"""]
    part1_answers = [15]
    part2_answers = [12]

    def parse1(self):
        matches = []
        for line in self.file.readlines():
            opp, you = line.strip().split(' ')
            match opp:
                case "A":
                    opp = Action.Rock
                case "B":
                    opp = Action.Paper
                case "C":
                    opp = Action.Scissors
            match you:
                case "X":
                    you = Action.Rock
                case "Y":
                    you = Action.Paper
                case "Z":
                    you = Action.Scissors
            matches.append((opp, you))
        return matches

    def parse2(self):
        matches = []
        for line in self.file.readlines():
            opp, outcome = line.strip().split(' ')
            match opp:
                case "A":
                    opp = Action.Rock
                case "B":
                    opp = Action.Paper
                case "C":
                    opp = Action.Scissors
            match outcome:
                case "X":
                    outcome = Result.Loss
                case "Y":
                    outcome = Result.Draw
                case "Z":
                    outcome = Result.Victory
            matches.append((opp, outcome))
        return matches

    @staticmethod
    def victor(a, b):
        if a==b:
            return Result.Draw
        elif a == uppermod(b+1, 3):
            return Result.Loss
        else:
            return Result.Victory

    @staticmethod
    def derive(a, b):
        if b == Result.Loss:
            return uppermod(a - 1, 3)
        elif b == Result.Victory:
            return uppermod(a + 1, 3)
        else:
            return a

    def part1(self):
        matches = self.parse1()
        choices = sum(m[1] for m in matches)
        results = sum(self.victor(*m) for m in matches)
        return choices + results

    def part2(self):
        games = self.parse2()
        matches = [(a,self.derive(a,b)) for a,b in games]

        choices = sum(m[1] for m in matches)
        results = sum(self.victor(*m) for m in matches)
        return choices + results
