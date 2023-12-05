import re


def part_one(filename):
    lookup = {
        "red": {"pattern": re.compile(r"(\d+)\s*red"), "count": 12},
        "green": {"pattern": re.compile(r"(\d+)\s*green"), "count": 13},
        "blue": {"pattern": re.compile(r"(\d+)\s*blue"), "count": 14},
    }
    games = load_game(filename)
    possible_games = []
    for game in games:
        game_id = int(re.compile(r"Game (\d+):").search(game).group(1))
        possible_games.append(game_id)
        for _, val in lookup.items():
            cubes = val["pattern"].findall(game)
            for cube in cubes:
                if int(cube) > val["count"] and game_id in possible_games:
                    possible_games.pop()

    return sum(possible_games)


def load_game(filename):
    with open(file=filename, mode="r") as f:
        games = f.read().split("\n")
    return games


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("------Part One-----")
    print(part_one(input_path))
