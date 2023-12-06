from collections import defaultdict
import math
import re

CUBE_LOOKUP = {
    "red": {"pattern": re.compile(r"(\d+)\s*red"), "count": 12},
    "green": {"pattern": re.compile(r"(\d+)\s*green"), "count": 13},
    "blue": {"pattern": re.compile(r"(\d+)\s*blue"), "count": 14},
}


def part_one(filename):
    games = load_game(filename)
    possible_games = []
    for game in games:
        game_id = int(re.compile(r"Game (\d+):").search(game).group(1))
        possible_games.append(game_id)
        for _, val in CUBE_LOOKUP.items():
            cubes = val["pattern"].findall(game)
            for cube in cubes:
                if int(cube) > val["count"] and game_id in possible_games:
                    possible_games.pop()

    return sum(possible_games)


def part_two(filename):
    games = load_game(filename)
    possible_games = defaultdict(dict)
    for game in games:
        game_id = int(re.compile(r"Game (\d+):").search(game).group(1))
        for key, val in CUBE_LOOKUP.items():
            cubes = val["pattern"].findall(game)
            possible_games[game_id][key] = max([int(cube) for cube in cubes])

    return sum([math.prod(game.values()) for game in possible_games.values()])


def load_game(filename):
    with open(file=filename, mode="r") as f:
        games = f.read().split("\n")
    return games


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
