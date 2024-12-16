def main():

    def problem1(rules, page_list) -> int:
        result = 0
        for pages in page_list:
            if is_ordered(rules, pages):
                midpoint = len(pages) // 2
                result += int(pages[midpoint])
        return result

    def problem2(rules, page_list) -> int:
        not_ordered = []
        for pages in page_list:
            if not is_ordered(rules, pages):
                not_ordered.append(pages)
        result = 0
        for pages in not_ordered:
            while not is_ordered(rules, pages):
                for i in range(len(pages)):
                    for j in range(i + 1, len(pages)):
                        if pages[j] in rules and pages[i] in rules[pages[j]]:
                            pages[j], pages[i] = pages[i], pages[j]
            midpoint = len(pages) // 2
            result += int(pages[midpoint])
        return result

    def is_ordered(rules, pages) -> bool:
        for page in pages:
            if page in rules:
                for num in rules[page]:
                    try:
                        if pages.index(num) < pages.index(page):
                            return False
                    except:
                        continue
        return True

    with open("../inputs/day5.txt") as file:
        lines = [line.strip() for line in file.readlines()]

        rules = []
        pages = []
        ruleset = {}

        is_rule = True
        for str in lines:
            if str == "":
                is_rule = False
                continue

            if is_rule:
                rules.append(str)
            else:
                pages.append(str.split(","))

        for rule in rules:
            nums = rule.split("|")
            if nums[0] not in ruleset:
                ruleset[nums[0]] = [nums[1]]
            else:
                ruleset[nums[0]].append(nums[1])

        answer1 = problem1(ruleset, pages)
        print(f"The answer to the first problem is {answer1}")

        answer2 = problem2(ruleset, pages)
        print(f"The answer to problem2 is {answer2}")


if __name__ == "__main__":
    main()
