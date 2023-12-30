from collections import deque


def part_one(filename):
    grid = load_grid(filename)

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                sr = r
                sc = c
                break

    # use bfs for path finding
    seen = set({(sr, sc)})
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        # Check each of the four directions
        # 1. Go up if char can go up and char above can receive upwards motion
        if (
            r > 0
            and ch in "S|JL"
            and grid[r - 1][c] in "|7F"
            and (r - 1, c) not in seen
        ):
            seen.add((r - 1, c))
            q.append((r - 1, c))

        # Check downwards motion
        # 2. Go down if char can go down and char below can receive downwards motion
        if (
            r < len(grid) - 1
            and ch in "S|7F"
            and grid[r + 1][c] in "|JL"
            and (r + 1, c) not in seen
        ):
            seen.add((r + 1, c))
            q.append((r + 1, c))

        # Check leftwards motion
        # 3. Go left if char can go left and char to the left can receive leftwards motion
        if (
            c > 0
            and ch in "S-J7"
            and grid[r][c - 1] in "-LF"
            and (r, c - 1) not in seen
        ):
            seen.add((r, c - 1))
            q.append((r, c - 1))

        # Check rightwards motion
        # 4. Go right if char can go right and char to the right can receive rightwards motion
        if (
            c < len(grid[0]) - 1
            and ch in "S-LF"
            and grid[r][c + 1] in "-J7"
            and (r, c + 1) not in seen
        ):
            seen.add((r, c + 1))
            q.append((r, c + 1))

    return len(seen) // 2


def part_two(filename):
    pass


def load_grid(filename):
    with open(file=filename, mode="r") as f:
        grid = f.read().splitlines()
    return grid


if __name__ == "__main__":
    input_path = "./day_10/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
