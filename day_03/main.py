from collections import deque


def part_one(filename):
    schematics = load_engine(filename)
    matrix = [[char for char in row] for row in schematics]
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    visited = set()

    def is_valid_symbol(c):
        return not (c.isdigit() or c == ".")

    def is_adjancent_to_symbol(r, c):
        for dr, dc in directions:
            if (
                0 <= r + dr < rows
                and 0 <= c + dc < cols
                and is_valid_symbol(matrix[r + dr][c + dc])
            ):
                return True
        return False

    total = 0
    for i, row in enumerate(matrix):
        j = 0
        while j < len(row):
            if row[j].isdigit() and (i, j) not in visited:
                number, start = row[j], j
                while j + 1 < len(row) and row[j + 1].isdigit():
                    j += 1
                    number += row[j]

                for col in range(start, j + 1):
                    visited.add((i, col))
                    if is_adjancent_to_symbol(i, col):
                        total += int(number)
                        break
            j += 1

    return total


def load_engine(filename):
    with open(file=filename, mode="r") as f:
        engines = f.read().split("\n")
    return engines


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("------Part One-----")
    print(part_one(input_path))
