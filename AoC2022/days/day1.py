from AoC2022.base.day import Day


class Day1(Day):
    tests = ["""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""]
    part1_answers = [24000]
    part2_answers = [45000]

    def parse(self):
        elves = [0]
        for line in self.file.readlines():
            if line.strip() == "":
                elves.append(0)
            else:
                elves[-1] += int(line.strip())
        elves.pop(0)
        return elves

    def part1(self):
        elves = self.parse()
        return max(elves)

    def part2(self):
        elves = self.parse()
        return sum(sorted(elves)[-3:])
