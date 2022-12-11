from AoC2022.base.day import Day


class Day8(Day):
    tests = ["""30373
25512
65332
33549
35390"""]
    part1_answers = [21]
    part2_answers = [8]

    def parse(self):
        return [list(map(int, x.strip())) for x in self.file.readlines()]

    def transform(self, key: (int, int), rotation):
        if rotation == 0:
            return key
        elif rotation == 1:
            return key[0], -1-key[1]
        elif rotation == 2:
            return key[1], key[0]
        elif rotation == 3:
            return -1-key[1], key[0]

    def part1(self):
        trees = self.parse()
        # All of this assumes that it is square
        side = len(trees)
        assert all(side == len(trees[i]) for i in range(side))
        visible = [[0 for i in row] for row in trees]

        for direction in range(4):
            for x in range(side):
                max = -1
                for y in range(side):
                    row, col = self.transform((x,y), direction)
                    if trees[row][col] > max:
                        max = trees[row][col]
                        visible[row][col] = 1
        # for i in visible:
        #     for j in i:
        #         print(j, end="")
        #     print()
        return sum(sum(x) for x in visible)
