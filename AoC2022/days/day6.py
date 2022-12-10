from AoC2022.base.day import Day


class Day6(Day):
    tests = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb","bvwbjplbgvbhsrlpgdmjqwftvncz","nppdvjthqldpwncqszvftbrmjlhg","nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg","zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
    part1_answers = [7,5,6,10,11]
    part2_answers = [19,23,23,29,26]

    def parse(self):
        return self.file.read().strip()

    def part1(self):
        data = self.parse()
        for i in range(len(data)):
            marker = data[i:i+4]
            if len(set(marker)) == 4:
                return i+4

    def part2(self):
        data = self.parse()
        for i in range(len(data)):
            marker = data[i:i+14]
            if len(set(marker)) == 14:
                return i+14
