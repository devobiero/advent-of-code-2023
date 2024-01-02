def part_one(filename):
    blocks = load_mirror(filename)

    def find_mirror(grid):
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]

            above = above[: len(below)]
            below = below[: len(above)]

            if above == below:
                return r
        return 0

    total = 0
    for block in blocks:
        row = find_mirror(block)
        total += row * 100

        col = find_mirror(list(zip(*block)))
        total += col

    return total


def part_two(filename):
    blocks = load_mirror(filename)

    def find_mirror(grid):
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]

            above = above[: len(below)]
            below = below[: len(above)]

            if (
                sum(
                    sum(0 if a == b else 1 for a, b in zip(x, y))
                    for x, y in zip(above, below)
                )
                == 1
            ):
                return r
        return 0

    total = 0
    for block in blocks:
        row = find_mirror(block)
        total += row * 100

        col = find_mirror(list(zip(*block)))
        total += col

    return total


def load_mirror(filename):
    with open(file=filename, mode="r") as f:
        mirrors = f.read().split("\n\n")
    return [mirror.splitlines() for mirror in mirrors]


if __name__ == "__main__":
    input_path = "./day_13/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
