if __name__ == "__main__":
    # Open the file in read mode
    with open("input.txt", "r") as file:
        # Read the content of the file
        content = file.read()

    # Split the content by newline characters to get individual numbers
    numbers = content.split("\n")

    max = 0
    sum = 0
    elves = []
    for num in numbers:
        if num.strip() != "":  # it is not a blank line
            sum += int(num.strip())
        else:
            # reached a blank line
            elves.append(sum)

            # Reset sum for next bag
            sum = 0

    elves.sort(reverse=True)
    result = elves[0] + elves[1] + elves[2]
    print(result)
