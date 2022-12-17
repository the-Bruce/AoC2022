from operator import attrgetter, itemgetter

from AoC2022.base.day import Day


def astar(map, start, target):
    def h(pos):
        # (taxirank metric + positive height delta) as heuristic
        tx, ty = target
        px, py = pos
        height_delta = max(0, map[tx][ty] - map[px][py] - 1)
        space_delta = abs(tx - px) + abs(ty - py)
        x = max(height_delta, space_delta)
        # print(x)
        return x

    def f(cur, pos):
        return 1

    def within(pos):
        px, py = pos
        return 0 <= px < len(map) and 0 <= py < len(map[0])

    def reachable(current, candidiate):
        return map[current[0]][current[1]] +1 >= map[candidiate[0]][candidiate[1]]

    queue = [(start, 0, 0, [start])]
    visited = [[False for _ in row] for row in map]
    while len(queue) > 0:
        current, cost, steps, route = queue.pop(0)
        cx, cy = current
        if current == target:
            # assert len(route) == steps+1
            return steps
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        neighbours = [(cx, cy - 1), (cx, cy + 1), (cx - 1, cy), (cx + 1, cy)]
        neighbours = [n for n in neighbours if within(n)]
        neighbours = [n for n in neighbours if reachable(current, n)]
        neighbours = [n for n in neighbours if not visited[n[0]][n[1]]]
        candidates = [(n, h(n) + f(current, n) + steps, f(current, n) + steps, None) for n in neighbours]
        queue.extend(candidates)
        queue.sort(key=itemgetter(1))
    return None

class Day12(Day):
    tests = ["""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""]
    part1_answers = [31]
    part2_answers = [29]

    def parse(self):
        height_map = [[ord(x) - ord('a') for x in f] for f in self.file.read().strip().splitlines(False)]
        start = None
        end = None
        for x, row in enumerate(height_map):
            for y, val in enumerate(row):
                if val == (ord('S') - ord('a')):
                    height_map[x][y] = 0
                    start = (x, y)
                elif val == (ord('E') - ord('a')):
                    height_map[x][y] = ord('z') - ord('a')
                    end = (x, y)
        assert start is not None
        assert end is not None
        return height_map, start, end

    def part1(self):
        map, start, end = self.parse()
        return astar(map, start, end)

    def part2(self):
        map, _, end = self.parse()

        lens = []
        for x, row in enumerate(map):
            for y, cell in enumerate(row):
                if cell == 0:
                    lens.append(astar(map, (x,y), end))
        return min([l for l in lens if l is not None])
