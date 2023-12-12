"""

dest, src, len
50 98 2 => src: 98, 99 dest: 50, 51
52 50 48 => src: 50, 51, 52, 53,...97 dest: 52, 53, 54, 55...99
"""


def part_one(filename):
    seeds, *blocks = load_seeds(filename)
    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        new = []
        for x in seeds:
            for a, b, c in ranges:
                if x in range(b, b + c):
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new

    return min(seeds)


def part_two(filename):
    pass


def load_seeds(filename):
    with open(file=filename, mode="r") as f:
        lines = f.read().split("\n\n")
    return lines


if __name__ == "__main__":
    input_path = "./day_05/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
