import math
import operator
from copy import deepcopy
from functools import partial

import tqdm as tqdm

from AoC2022.base.day import Day


class Monkey:
    def __init__(self, starting, action, test, tru, flse):
        self.items = starting
        self.action = action
        self.test = test
        self.true = tru
        self.false = flse
        self.inspections = 0

    def catch(self, item):
        self.items.append(item)

    def act(self, monkeys, calmness = 3, field = None):
        for item in self.items:
            self.inspections += 1
            # print(f"inspect {item}")
            item = self.action(item)
            # print(f"act {item}")
            item = item // calmness
            if field:
                item = item % field
            # print(f"relax {item}")
            if item % self.test == 0:
                # print("true")
                monkeys[self.true].catch(item)
            else:
                # print("false")
                monkeys[self.false].catch(item)
        self.items = []


def lookup_op(op):
    if op == "+":
        return operator.add
    elif op == "*":
        return operator.mul
    elif op == "-":
        return operator.sub
    else:
        raise NotImplementedError(op)


class Day11(Day):
    tests = ["""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""]
    part1_answers = [10605]
    part2_answers = [2713310158]

    def parse(self):
        file = self.file.read()
        monkeyspecs = file.split('\n\n')
        monkeys = []
        for monkey in monkeyspecs:
            starting, op, test, tru, flse = [[i.strip() for i in l.strip().split(':')[1:]].pop() for l in
                                             monkey.splitlines()][1:]
            starting = starting.split(', ')
            starting = list(map(int, starting))

            arg1, op, arg2 = op.split()[2:]
            d = {}
            exec(compile(f"""def f(old):
               return {arg1} {op} {arg2}""", "<compiled>", "exec"),{},d)
            action = deepcopy(d['f'])
            del d
            # print(action)
            # if arg2 == "old":
            #
            # else:
            #     action = partial(lambda f, a, x: f(x, a), f, int(arg2))

            _, _, test = test.split()
            test = int(test)
            _, _, _, tru = tru.split()
            tru = int(tru)
            _, _, _, flse = flse.split()
            flse = int(flse)
            monkeys.append(Monkey(starting, action, test, tru, flse))
        return monkeys

    def part1(self):
        monkeys = self.parse()
        for i in range(20):
            for monkey in monkeys:
                monkey.act(monkeys)
            # print(i)
            # for j, monkey in enumerate(monkeys):
            #     print(j, monkey.items)
        inspections = sorted([monkey.inspections for monkey in monkeys])
        # print(inspections)
        return operator.mul(*inspections[-2:])

    def part2(self):
        monkeys = self.parse()
        divisor = math.lcm(*(monkey.test for monkey in monkeys))
        for i in tqdm.tqdm(range(10000)):
            for monkey in monkeys:
                monkey.act(monkeys, calmness=1, field=divisor)
            # print(i)
            # for j, monkey in enumerate(monkeys):
            #     print(j, monkey.items)
        inspections = sorted([monkey.inspections for monkey in monkeys])
        return operator.mul(*inspections[-2:])
