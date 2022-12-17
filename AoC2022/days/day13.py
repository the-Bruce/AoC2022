import ast
from enum import IntEnum
from functools import cmp_to_key
from itertools import zip_longest

from AoC2022.base.day import Day


class Ord(IntEnum):
    WRONG = -1
    PENDING = 0
    RIGHT = 1


def compare(left, right):
    if right is None:
        return Ord.WRONG
    elif left is None:
        return Ord.RIGHT

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Ord.RIGHT
        elif left == right:
            return Ord.PENDING
        else:
            return Ord.WRONG

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for l, r in zip_longest(left, right):
        comp = compare(l, r)
        if comp != Ord.PENDING:
            return comp
    return Ord.PENDING


class Day13(Day):
    tests = ["""[[1],[2,3,4]]
[[1],4]""", """[9]
[[8,7,6]]""", """[[4,4],4,4]
[[4,4],4,4,4]""", """[7,7,7,7]
[7,7,7]""", """[]
[3]""", """[[[]]]
[[]]""", """[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""", """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""]
    part1_answers = [1, 0, 1, 0, 1, 0, 0, 13]
    part2_answers = [None, None, None, None, None, None, None, 140]

    def parse(self):
        def convert(v):
            try:
                return ast.literal_eval(v)  # This is awful... I love it!
            except SyntaxError:
                print(v)
                raise

        file = self.file.read()
        pairs = [tuple(convert(x) for x in mp.split('\n')[:2]) for mp in file.split("\n\n")]
        return pairs

    def part1(self):
        messages = self.parse()
        result = 0
        for index, m in enumerate(messages):
            m1, m2 = m
            if compare(m1, m2) == Ord.RIGHT:
                result += (index + 1)
        return result

    def part2(self):
        messages = self.parse()
        messages.append(([[2]], [[6]]))
        allmessages = []
        for m1, m2 in messages:
            allmessages.append(m1)
            allmessages.append(m2)
        allmessages.sort(key=cmp_to_key(compare), reverse=True)
        a = allmessages.index([[2]])
        b = allmessages.index([[6]])
        return (a+1)*(b+1)
