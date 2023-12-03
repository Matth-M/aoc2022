def compute_score(opponent_play: str, your_play: str) -> int:
    if opponent_play == "A":
        if your_play == "X":
            return 4
        elif your_play == "Y":
            return 8
        elif your_play == "Z":
            return 3
    elif opponent_play == "B":
        if your_play == "X":
            return 1
        elif your_play == "Y":
            return 5
        elif your_play == "Z":
            return 9
    elif opponent_play == "C":
        if your_play == "X":
            return 7
        elif your_play == "Y":
            return 2
        elif your_play == "Z":
            return 6
    return 0


def compute_score2(opponent_play: str, expected_outcome: str) -> int:
    if opponent_play == "A":
        if expected_outcome == "X":
            return compute_score(opponent_play, "Z")
        elif expected_outcome == "Y":
            return compute_score(opponent_play, "X")
        elif expected_outcome == "Z":
            return compute_score(opponent_play, "Y")
    elif opponent_play == "B":
        if expected_outcome == "X":
            return compute_score(opponent_play, "X")
        elif expected_outcome == "Y":
            return compute_score(opponent_play, "Y")
        elif expected_outcome == "Z":
            return compute_score(opponent_play, "Z")
    elif opponent_play == "C":
        if expected_outcome == "X":
            return compute_score(opponent_play, "Y")
        elif expected_outcome == "Y":
            return compute_score(opponent_play, "Z")
        elif expected_outcome == "Z":
            return compute_score(opponent_play, "X")
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()

    rounds = content.split("\n")
    rounds.pop()  # Remove empty line

    score1 = 0
    score2 = 0
    for round in rounds:
        plays = round.split()
        score1 += compute_score(plays[0], plays[1])
        score2 += compute_score2(plays[0], plays[1])
        print(score2, plays[1])

    print(score2)
