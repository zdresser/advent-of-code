def problem_1(input):
    safe_arrays = 0
    for arr in input:
        safe_arrays += check_if_safe(arr)
    print(f"Problem 1: {safe_arrays}")


def problem_2(input):
    safe_arrays = 0
    for arr in input:
      safe_arrays += check_if_safe_2(arr)
    print(f"Problem 2: {safe_arrays}")


def main():
    input = []
    with open("../inputs/day2.txt") as file:
        for line in file:
            split = line.split()
            to_int = [int(item) for item in split]
            input.append(to_int)
    problem_1(input)
    problem_2(input)

def check_if_safe(input):
    is_increasing = input[1] > input[0]
    if is_increasing:
        for i in range(1, len(input)):
            diff = input[i] - input[i-1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(input)):
            diff = input[i] - input[i-1]
            if not -3 <= diff <= -1:
                return False
        return True
def check_if_safe_2(arr):
  if check_if_safe(arr):
    return True
  for i in range(len(arr)):
    if check_if_safe(arr[:i] + arr[i+1:]):
        return True
  return False

if __name__ == "__main__":
    main()
