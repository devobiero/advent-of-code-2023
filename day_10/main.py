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
    grid = load_grid(filename)

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                sr = r
                sc = c
                break

    # use bfs for path finding
    loop = set({(sr, sc)})
    q = deque([(sr, sc)])

    maybe_s = set({"|", "-", "7", "J", "L", "F"})

    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        if (
            r > 0
            and ch in "S|JL"
            and grid[r - 1][c] in "|7F"
            and (r - 1, c) not in loop
        ):
            loop.add((r - 1, c))
            q.append((r - 1, c))

            # set intersection
            if ch == "S":
                maybe_s &= {"|", "J", "L"}

        if (
            r < len(grid) - 1
            and ch in "S|7F"
            and grid[r + 1][c] in "|JL"
            and (r + 1, c) not in loop
        ):
            loop.add((r + 1, c))
            q.append((r + 1, c))

            if ch == "S":
                maybe_s &= {"|", "7", "F"}

        if (
            c > 0
            and ch in "S-J7"
            and grid[r][c - 1] in "-LF"
            and (r, c - 1) not in loop
        ):
            loop.add((r, c - 1))
            q.append((r, c - 1))

            if ch == "S":
                maybe_s &= {"-", "J", "7"}

        if (
            c < len(grid[0]) - 1
            and ch in "S-LF"
            and grid[r][c + 1] in "-J7"
            and (r, c + 1) not in loop
        ):
            loop.add((r, c + 1))
            q.append((r, c + 1))

            if ch == "S":
                maybe_s &= {"-", "L", "F"}

    assert len(maybe_s) == 1
    (S,) = maybe_s

    # replace "S" with correct char
    grid = [row.replace("S", S) for row in grid]

    # replace garbage pipes with dots
    grid = [
        "".join(ch if (r, c) in loop else "." for c, ch in enumerate(row))
        for r, row in enumerate(grid)
    ]

    # invalid / outside points
    outside = set()

    for r, row in enumerate(grid):
        up = None
        within = False
        for c, ch in enumerate(row):
            # Check vertical pipe
            if ch == "|":
                assert up is None
                within = not within
            # Horizontal pipe
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "J7":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"Unexpected horizontal character: {ch}")
            if not within:
                outside.add((r, c))

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            print("#" if (r, c) in outside - loop else ".", end="")
        print()

    return len(grid) * len(grid[0]) - len(outside | loop)


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
