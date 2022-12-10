from functools import partial
from operator import ge

from AoC2022.base.day import Day


class Dir:
    def __init__(self, parent, name):
        if parent is None:
            self.alldirs = []
        self.parent = parent
        self.name = name
        self.files: dict[str, int] | None = None
        self.folders: dict[str, Dir] | None = None

        self.register(self)

    def register(self, obj):
        if self.parent is None:
            self.alldirs.append(obj)
        else:
            self.parent.register(obj)

    def ls(self, contents: list[tuple[str, str]]):
        if self.files is not None:
            raise ValueError("Double ls")
        self.files = {}
        self.folders = {}
        for stype, inode in contents:
            if stype == "dir":
                self.folders[inode] = Dir(self, inode)
            else:
                self.files[inode] = int(stype)

    def pwd(self):
        if self.parent is not None:
            return f"{self.parent.pwd()}/{self.name}"
        else:
            return f"/{self.name}"

    def size(self):
        assert self.files is not None
        return sum(self.files.values()) + sum(map(lambda x: x.size(), self.folders.values()))

    def cd(self, name):
        if name == '..':
            return self.parent
        elif name == '.':
            return self
        else:
            return self.folders[name]

    def tree(self, prefix = ''):
        print(prefix+self.name)
        for file, size in self.files.items():
            print(prefix+" "+file, f"({size})")
        for dir in self.folders.values():
            dir.tree(prefix+" ")


class Day7(Day):
    tests = ["""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""]
    part1_answers = [95437]
    part2_answers = [24933642]

    def parse(self):
        assert self.file.readline().strip() == "$ cd /"  # skip the first line
        ops = []
        op = "cd"
        args = ["/"]
        res: list[(str, str)] = []
        for line in self.file.readlines():
            line = line.strip()
            line = list(map(lambda x: x.strip(), line.split()))
            if line[0] == "$":
                ops.append((op, args, res))
                op = line[1]
                args = line[2:]
                res = []
            else:
                res.append(tuple(line))
        ops.append((op, args, res))
        return ops

    def builddir(self):
        actions = self.parse()
        actions.pop(0)
        wd = Dir(None, '')
        root = wd
        for command, args, result in actions:
            if command == "cd":
                wd = wd.cd(args[0])
            elif command == "ls":
                wd.ls(result)
        return root

    def part1(self):
        root = self.builddir()
        # filter(partial(ge, 100000), map(lambda x: x.size(), root.alldirs))
        return sum([x.size() for x in root.alldirs if x.size() < 100000])

    def part2(self):
        root = self.builddir()
        size = root.size()
        free = 70000000 - size
        needed = 30000000 - free
        return min([x.size() for x in root.alldirs if x.size() > needed])
