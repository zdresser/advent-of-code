def problem_1(hash, lines):
    print(hash)
    print(lines)
    xmas_total = 0
    for line, value in enumerate(lines):

        for idx, char in enumerate(value):

            if char == "X":
                # check cardinal directions
                # right
                if (
                    hash.get((line, idx + 1)) == "M"
                    and hash.get((line, idx + 2)) == "A"
                    and hash.get((line, idx + 3)) == "S"
                ):
                    xmas_total += 1
                # left
                if (
                    hash.get((line, idx - 1)) == "M"
                    and hash.get((line, idx - 2)) == "A"
                    and hash.get((line, idx - 3)) == "S"
                ):
                    xmas_total += 1
                # up
                if (
                    hash.get((line + 1, idx)) == "M"
                    and hash.get((line + 2, idx)) == "A"
                    and hash.get((line + 3, idx)) == "S"
                ):

                    xmas_total += 1
                # down
                if (
                    hash.get((line - 1, idx)) == "M"
                    and hash.get((line - 2, idx)) == "A"
                    and hash.get((line - 3, idx)) == "S"
                ):

                    xmas_total += 1
                    # check diagonals
                    # up-right
                if (
                    hash.get((line + 1, idx + 1)) == "M"
                    and hash.get((line + 2, idx + 2)) == "A"
                    and hash.get((line + 3, idx + 3)) == "S"
                ):

                    xmas_total += 1
                    # down-left
                if (
                    hash.get((line - 1, idx - 1)) == "M"
                    and hash.get((line - 2, idx - 2)) == "A"
                    and hash.get((line - 3, idx - 3)) == "S"
                ):

                    xmas_total += 1
                    # up-left
                if (
                    hash.get((line + 1, idx - 1)) == "M"
                    and hash.get((line + 2, idx - 2)) == "A"
                    and hash.get((line + 3, idx - 3)) == "S"
                ):

                    xmas_total += 1
                    # down-right
                if (
                    hash.get((line - 1, idx + 1)) == "M"
                    and hash.get((line - 2, idx + 2)) == "A"
                    and hash.get((line - 3, idx + 3)) == "S"
                ):

                    xmas_total += 1

    return xmas_total


def create_hash_map(lines):
    result = {}
    for line, value in enumerate(lines):
        for idx, char in enumerate(value):
            result[line, idx] = char
    return result


def main():
    with open("../inputs/day4.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        padded_lines = ["...." + line + "...." for line in lines]

        for i in range(4):
            padded_lines.insert(0, "." * 18)
            padded_lines.append("." * 18)
        hash_map = create_hash_map(lines)

        answer_1 = problem_1(hash_map, lines)
        print(f"The answer to Problem 1 is {answer_1}")


if __name__ == "__main__":
    main()
