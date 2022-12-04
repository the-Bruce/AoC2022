from AoC2022.base.day import Day


class Day4(Day):
    tests = ["""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""", "5-6,6-6"]
    part1_answers = [2, 1]
    part2_answers = [4, 1]

    def parse(self):
        ranges = []
        for line in self.file.readlines():
            line = line.strip()
            ranges.append(tuple(map(lambda x: tuple(map(int, x.split('-'))), line.split(','))))
        return ranges

    @staticmethod
    def between(a, b):
        x1, y1 = a
        x2, y2 = b
        return x2 <= x1 and y1 <= y2

    @staticmethod
    def intersects(a,b):
        x1, y1 = a
        x2, y2 = b
        return x2 <= x1 <= y2 or x2 <= y1 <= y2

    def part1(self):
        ranges = self.parse()
        return sum(1 for x, y in ranges if self.between(x, y) or self.between(y, x))

    def part2(self):
        ranges = self.parse()
        return sum([1 for x, y in ranges if self.intersects(x, y) or self.intersects(y, x)])
