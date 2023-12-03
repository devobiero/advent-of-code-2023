"""
link: https://adventofcode.com/2023/day/1

Example:

Part one:
1abc2 = 12
pqr3stu8vwx = 38
a1b2c3d4e5f = 15
treb7uchet = 77

result = 12 + 38 + 15 + 77 = 142

Part two:
two1nine = 29
eightwothree = 83
abcone2threexyz = 13
xtwone3four = 24
4nineeightseven2 = 42
zoneight234 = 14
7pqrstsixteen = 76

result = 29 + 83 + 13 + 24 + 42 + 14 + 76 = 281
"""


def part_one(filename):
    calibrations = load_calibrations(filename)

    def digit_from_left(calibration):
        left = 0

        while left < len(calibration):
            if calibration[left].isdigit():
                return calibration[left]
            left += 1

        return "0"

    def digit_from_right(calibration):
        right = len(calibration) - 1

        while right >= 0:
            if calibration[right].isdigit():
                return calibration[right]
            right -= 1

        return "0"

    def extract_digits(calibration):
        return "".join([digit_from_left(calibration), digit_from_right(calibration)])

    return sum([int(extract_digits(calibration)) for calibration in calibrations])


def part_two(filename):
    calibrations = load_calibrations(filename)

    def word_to_number(word):
        lookup = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        lower_case_word = word.lower()
        return lookup.get(lower_case_word, None)

    def digit_from_left(calibration):
        left = 0
        n = len(calibration)

        while left < n:
            right = left + 1
            while right <= n:
                substring = calibration[left:right]
                if substring.isdigit():
                    return str(substring)

                numeric_equiv = word_to_number(substring)
                if numeric_equiv:
                    return str(numeric_equiv)

                right += 1
            left += 1

        return "0"

    def digit_from_right(calibration):
        n = len(calibration)
        left = n
        while left >= 0:
            right = left - 1
            while right >= 0:
                substring = calibration[right:left]
                if substring.isdigit():
                    return str(substring)

                numeric_equiv = word_to_number(substring)
                if numeric_equiv:
                    return str(numeric_equiv)

                right -= 1
            left -= 1

        return "0"

    def extract_digits(calibration):
        return "".join([digit_from_left(calibration), digit_from_right(calibration)])

    return sum([int(extract_digits(calibration)) for calibration in calibrations])


def load_calibrations(filename):
    with open(file=filename, encoding="utf-8") as f:
        lines = f.read().split("\n")
    return lines


if __name__ == "__main__":
    input_path = "./day_01/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
