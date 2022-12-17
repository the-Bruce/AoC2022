from AoC2022.base.day import Day


class Day12(Day):
    tests = ["""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""]
    part1_answers = [31]
    part2_answers = []

    def parse(self):
        return [list(f) for f in self.file.read().strip().splitlines(False)]

    def part1(self):
        print(self.parse())
