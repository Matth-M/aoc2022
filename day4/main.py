"""DAY4 AOC"""


def letter_priority(letter: str):
    if len(letter) != 1:
        raise ValueError("Input should be a single letter")
    if letter.islower():
        offset = 96
    else:
        offset = 64 - 26  # Capital letters start at a priority of A: 27
    return ord(letter) - offset


def find_common_letter(backpack: str) -> str:
    half_backpack_len = len(backpack) // 2
    compartments = [
        list(backpack[:half_backpack_len]),
        list(backpack[half_backpack_len:]),
    ]

    for letter in compartments[0]:
        if letter in compartments[1]:
            return letter
    raise ValueError("Incorrect input")


def common_letter_multiple_backpacks(backpacks: list[str]) -> str:
    for letter in backpacks[0]:
        if letter in backpacks[1] and letter in backpacks[2]:
            return letter
    return ""


def part_one(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    score = 0
    for backpack in lines:
        common_letter = find_common_letter(backpack)
        score += letter_priority(common_letter)
    return score


def part_two(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    score = 0
    for i in range(0, len(lines) - 1, 3):
        backpacks = [lines[i], lines[i + 1], lines[i + 2]]
        common_letter = common_letter_multiple_backpacks(backpacks)
        score += letter_priority(common_letter)

    return score


if __name__ == "__main__":
    input_file = "./input.txt"
    score = part_one(input_file)
    print(score)

    score = part_two(input_file)
    print(score)
