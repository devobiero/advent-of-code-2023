def part_one(filename):
    grid = load_grid(filename)

    # Find the shortest path, manhattan distance
    empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]

    points = [
        (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"
    ]

    total = 0
    scale = 1000000

    for i, (r1, c1) in enumerate(points):
        for r2, c2 in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1
    return total


def load_grid(filename):
    with open(file=filename, mode="r") as f:
        grid = f.read().splitlines()
    return grid


if __name__ == "__main__":
    input_path = "./day_11/input.txt"
    print("------Part One-----")
    print(part_one(input_path))
