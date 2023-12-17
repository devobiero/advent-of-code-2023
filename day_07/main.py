hands = [
    "Five of a kind",
    "Four of a kind",
    "Full house",
    "Three of a kind",
    "Two pair",
    "One pair",
    "High card",
]


def get_hand_type(hand, freqs):
    if 5 in freqs.values():
        return hands[0]
    elif 4 in freqs.values():
        return hands[1]
    elif 3 in freqs.values() and 2 in freqs.values():
        return hands[2]
    elif 3 in freqs.values():
        return hands[3]
    elif list(freqs.values()).count(2) == 2:
        return hands[4]
    elif 2 in freqs.values():
        return hands[5]
    else:
        return hands[6]


def part_one(filename):
    cards = [card.split(" ") for card in load_hands(filename)]
    results = []

    def hand_comparator(hand):
        return hands.index(hand[1])

    def card_comparator(card):
        cards_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        return [cards_order.index(char) for char in card[0]]

    for card in cards:
        hand = card[0]
        bid = card[1]
        freqs = dict()

        for c in hand:
            freqs[c] = freqs.get(c, 0) + 1
        results.append((hand, get_hand_type(hand, freqs), int(bid)))

    results.sort(key=lambda x: (hand_comparator(x), card_comparator(x)))

    winnings = 0
    for i, result in enumerate(results):
        rank = len(results) - i
        winnings += rank * result[2]

    return winnings


def part_two(filename):
    cards = [card.split(" ") for card in load_hands(filename)]
    results = []

    def hand_comparator(hand):
        return hands.index(hand[1])

    def card_comparator(card):
        cards_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        return [cards_order.index(char) for char in card[0]]

    for card in cards:
        hand = card[0]
        bid = card[1]
        freqs = dict()

        for c in hand:
            freqs[c] = freqs.get(c, 0) + 1

        nums = freqs.get("J", 0)
        if nums and nums < 5:
            # find the most frequent key which is not J
            max_key = max(
                ((key, value) for key, value in freqs.items() if key != "J"),
                key=lambda x: x[1],
            )[0]
            freqs[max_key] += nums
            del freqs["J"]

        results.append((hand, get_hand_type(hand, freqs), int(bid)))

    results.sort(key=lambda x: (hand_comparator(x), card_comparator(x)))

    winnings = 0
    for i, result in enumerate(results):
        rank = len(results) - i
        winnings += rank * result[2]

    return winnings


def load_hands(filename):
    with open(file=filename, mode="r") as f:
        lines = f.read().splitlines()
    return lines


if __name__ == "__main__":
    input_path = "./day_07/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
