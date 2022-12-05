from collections import defaultdict
from string import ascii_letters

from AoC2022.base.day import Day


class Day5(Day):
    tests = ["""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""]
    part1_answers = ["CMZ"]
    part2_answers = ["MCD"]

    def parse(self):
        instructions = []
        state = defaultdict(list)
        while (line:=self.file.readline()) != "\n":
            line = line.strip('\n')+' '
            blocks = zip(*(iter(line),) * 4)
            for i,(_,l,_,_) in enumerate(blocks):
                if l in ascii_letters:
                    state[i+1].insert(0,l)
        for line in self.file.readlines():
            line = line.strip()
            _,a,_,b,_,c = line.split(' ')
            instructions.append((int(a),int(b),int(c)))
        return instructions, state

    def part1(self):
        instructions, state = self.parse()
        for count, source, sink in instructions:
            for _ in range(count):
                state[sink].append(state[source].pop())

        res = ""
        for i in range(len(state)):
            res += state[i + 1].pop()
        return res

    def part2(self):
        instructions, state = self.parse()
        for count,source,sink in instructions:
            tmp = []
            for _ in range(count):
                tmp.append(state[source].pop())
            for _ in range(count):
                state[sink].append(tmp.pop())

        res = ""
        for i in range(len(state)):
            res += state[i+1].pop()
        return res
