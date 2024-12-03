import re
def clean_input(file) -> str:
  pattern = r"mul\((\d+),(\d+)\)"
  string_result = re.findall(pattern, file)
  int_result = [(int(a), int(b)) for a,b in string_result]
  return int_result

def add_multiples(arr):
  multiples = [a*b for a,b in arr]
  result = sum(multiples)
  return result

def problem_2(file):
  pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
  matches = re.findall(pattern, file)
  result = 0
  is_do= True
  for match in matches:
    if match == "do()":
      is_do = True
    elif match == "don't()":
      is_do = False
    else:
      if is_do:
        a,b = map(int, match[4:-1].split(","))
        result += a * b
  return result


def main():
  with open("../inputs/day3.txt", "r") as file:
    file = file.read()

    #problem 1
    cleaned_input = clean_input(file)
    problem1 = add_multiples(cleaned_input)
    print(f"Problem 1 answer is {problem1}")

    #problem 2
    problem_2_result = problem_2(file)
    print(f"Problem 2 answer is {problem_2_result}")

if __name__ == "__main__":
  main()