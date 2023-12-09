def is_one_contained(ranges: list[list[int]]) -> bool:
    if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
        return True
    if ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][1]:
        return True
    return False


def overlaps(ranges: list[list[int]]) -> bool:
    [bot_1, up_1] = ranges[0]
    [bot_2, up_2] = ranges[1]
    if up_2 < bot_1 or up_1 < bot_2:
        return False
    else:
        return True


def part_two(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file.readlines()]
    result = 0
    for line in lines:
        ranges = line.split(",")
        ranges = [range.split("-") for range in ranges]
        ranges = [
            [int(start), int(end)]
            for range_ in ranges
            if (start := range_[0].strip()) and (end := range_[1].strip())
        ]
        if overlaps(ranges):
            result += 1
    return result


def part_one(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file.readlines()]
    result = 0
    for line in lines:
        ranges = line.split(",")
        ranges = [range.split("-") for range in ranges]
        ranges = [
            [int(start), int(end)]
            for range_ in ranges
            if (start := range_[0].strip()) and (end := range_[1].strip())
        ]
        if is_one_contained(ranges):
            result += 1
    return result


if __name__ == "__main__":
    input_file = "./input.txt"
    score = part_one(input_file)
    print("part_one", score)

    score = part_two(input_file)
    print("part_two", score)
