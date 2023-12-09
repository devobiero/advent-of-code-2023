DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]


def part_one(filename):
    schematics = load_engine(filename)
    matrix = [[char for char in row] for row in schematics]
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def is_valid_symbol(c):
        return not (c.isdigit() or c == ".")

    def is_adjancent_to_symbol(r, c):
        for dr, dc in DIRECTIONS:
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


def part_two(filename):
    schematics = load_engine(filename)
    matrix = [[char for char in row] for row in schematics]

    def get_complete_number(row, col):
        number_str = matrix[row][col]

        # Scan from right to left
        left_col = col - 1
        while left_col >= 0 and matrix[row][left_col].isdigit():
            number_str = matrix[row][left_col] + number_str
            left_col -= 1

        # Scan from left to right
        right_col = col + 1
        while right_col < len(matrix[row]) and matrix[row][right_col].isdigit():
            number_str += matrix[row][right_col]
            right_col += 1

        return int(number_str)

    def get_gear_ratio(row, col):
        adjacent_numbers = []
        for dx, dy in DIRECTIONS:
            adjacent_row, adjacent_col = row + dx, col + dy
            if (
                0 <= adjacent_row < len(matrix)
                and 0 <= adjacent_col < len(matrix[adjacent_row])
                and matrix[adjacent_row][adjacent_col].isdigit()
            ):
                part_number = get_complete_number(adjacent_row, adjacent_col)
                if part_number not in adjacent_numbers:
                    adjacent_numbers.append(part_number)

        return (
            adjacent_numbers[0] * adjacent_numbers[1]
            if len(adjacent_numbers) == 2
            else 0
        )

    total_sum = 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            total_sum += get_gear_ratio(i, j) if char == "*" else 0

    return total_sum


def load_engine(filename):
    with open(file=filename, mode="r") as f:
        engines = f.read().split("\n")
    return engines


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
