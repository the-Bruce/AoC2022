import string

from AoC2022.base.day import Day


class Day3(Day):
    tests = ["""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""]
    part1_answers = [157]
    part2_answers = [70]

    def parse(self):
        sacks = []
        for line in self.file.readlines():
            line = line.strip()
            mid = (len(line)) // 2
            sacks.append((set(line[:mid]), set(line[mid:])))
        return sacks

    priorities = list(" "+string.ascii_letters)

    def char_to_priority(self,c):
        return self.priorities.index(c)

    def part1(self):
        sacks = self.parse()
        return sum(sum(map(self.char_to_priority, a.intersection(b))) for a,b in sacks)

    def part2(self):
        sacks = list(map(lambda x:x[0].union(x[1]), self.parse()))
        groups = zip(*(iter(sacks),) * 3) # break into three-tuples
        return sum(sum(map(self.char_to_priority, a.intersection(b).intersection(c))) for a,b,c in groups)
