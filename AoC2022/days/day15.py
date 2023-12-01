from tqdm import tqdm

from AoC2022.base.day import Day


def distance(pos1, pos2):
    (x1, y1), (x2, y2) = pos1, pos2
    return abs(x1 - x2) + abs(y1 - y2)


def sensor_range(reading):
    return distance(*reading)


def close_to(loc, reading):
    sensor, _ = reading
    range = sensor_range(reading)
    return distance(loc, sensor) <= range


def skip_x(loc, reading):
    sensor, _ = reading
    (x1, y1), (x2, y2) = loc, sensor
    if not close_to(loc, reading):
        return (x1, y1), 0
    elif x1 < x2:
        return (x2 + (x2 - x1), y1), (x2 + (x2 - x1)) - x1
    else:
        return (x1+1, y1), 1


class Day15(Day):
    # Note, this day has an additional argument concatenated to the start of the input for the line to check
    tests = ["""10
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""]
    part1_answers = [26]
    part2_answers = []

    def parse(self):
        row = int(self.file.readline().strip())
        sensors = []
        for line in self.file.readlines():
            _, _, x1, y1, _, _, _, _, x2, y2 = line.strip().split(' ')
            x1 = int(x1[2:-1])
            x2 = int(x2[2:-1])
            y1 = int(y1[2:-1])
            y2 = int(y2[2:])
            sensors.append(((x1, y1), (x2, y2)))
        return sensors, row

    def part1(self):
        readings, row = self.parse()
        beacons = [a[1] for a in readings]
        sensors = [a[0] for a in readings]
        max_range = max(sensor_range(x) for x in readings)
        maxx = max(max(x[0] for x in beacons), max(x[0] for x in sensors)) + max_range + 1
        minx = min(min(x[0] for x in beacons), min(x[0] for x in sensors)) - max_range - 1
        cells = 0
        # print(minx, maxx)
        coord = (minx - 1, row)
        while coord[0] <= maxx + 1:
            old = coord
            if coord not in beacons:
                for reading in readings:
                    coord, skipped = skip_x(coord, reading)
                    print(coord)
                    cells += skipped
            if coord == old:
                coord = coord[0] + 1, coord[1]
        return cells+1
