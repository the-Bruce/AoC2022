from operator import itemgetter

from AoC2022.base.day import Day


class Space:
    def __init__(self, xrange, yrange):
        self.minx, self.maxx = xrange
        self.miny, self.maxy = yrange
        # Inclusive to exclusive
        self.maxx += 1
        self.maxy += 1
        self._list = [[False for _ in range(self.minx, self.maxx)] for _ in range(self.miny, self.maxy)]

    def __getitem__(self, item):
        itemx, itemy = item
        if itemx >= self.maxx or itemx < self.minx:
            raise KeyError(f"Invalid x coordinate {itemx}")
        if itemy >= self.maxy or itemy < self.miny:
            raise KeyError(f"Invalid y coordinate {itemy}")
        return self._list[itemy - self.miny][itemx - self.minx]

    def __setitem__(self, item, value):
        itemx, itemy = item
        if itemx >= self.maxx or itemx < self.minx:
            raise KeyError(f"Invalid x coordinate {itemx}")
        if itemy >= self.maxy or itemy < self.miny:
            raise KeyError(f"Invalid y coordinate {itemy}")
        self._list[itemy - self.miny][itemx - self.minx] = value

    def count(self):
        return sum(sum(row) for row in self._list)

    def __str__(self):
        space = f"({self.minx},{self.miny}) -> ({self.maxx},{self.maxy})\n"
        for line in self._list:
            for x in line:
                space += '#' if x else " "
            space += '\n'
        return space


class Day14(Day):
    tests = ["""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""]
    part1_answers = [24]
    part2_answers = []

    def parse(self, floor=False):
        seams = []
        minx = 1000
        miny = 0
        maxx = maxy = -1000
        for line in self.file.readlines():
            coords = [tuple(int(z) for z in x.split(',')) for x in line.strip().split(' -> ')]
            print(coords)
            minx = min(minx, min(coords, key=itemgetter(0))[0])
            miny = min(miny, min(coords, key=itemgetter(1))[1])
            maxx = max(maxx, max(coords, key=itemgetter(0))[0])
            maxy = max(maxy, max(coords, key=itemgetter(1))[1])
            seams.extend(zip(coords, coords[1:]))
        print(seams)
        if floor:
            maxy += 2
            minx -= 150
            maxx += 200
            seams.append(((minx,maxy),(maxx, maxy)))
        space = Space((minx, maxx), (miny, maxy))
        for (startx, starty), (endx, endy) in seams:
            leastx, greatestx = sorted((startx, endx))
            leasty, greatesty = sorted((starty, endy))
            for x in range(leastx, greatestx + 1):
                for y in range(leasty, greatesty + 1):
                    space[x, y] = True
        print(space)
        return space

    def settle(self, space):
        motex, motey = (500, 0)
        while True:
            targetx, targety = motex, motey + 1
            # print(targetx, targety)
            if space[targetx, targety]:
                targetx -= 1
            else:
                motex, motey = targetx, targety
                continue
            if space[targetx, targety]:
                targetx += 2
            else:
                motex, motey = targetx, targety
                continue
            if space[targetx, targety]:
                return motex, motey
            else:
                motex, motey = targetx, targety

    def part1(self):
        space = self.parse()
        walls = space.count()
        try:
            while True:
                new_sand = self.settle(space)
                space[new_sand] = True
                print(space)
        except KeyError:
            return space.count() - walls

    def part2(self):
        space = self.parse(floor=True)
        walls = space.count()
        i=0
        try:
            while True:
                i+=1
                new_sand = self.settle(space)
                space[new_sand] = True
                # Uncomment to get cool animation
                # if i%10 == 0:
                #     print(space)
                if new_sand == (500,0):
                    return space.count() - walls
        except KeyError:
            raise
