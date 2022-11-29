#TEMPLATE FILE 
from util import helpers

test_cases = [ #add test cases here
  {
    "input": """
    """,
    "solution": 0
  }
]

OKGREEN = '\033[92m'
BOLD = '\033[1m'
ENDC = '\033[0m'
FAIL = '\033[91m'

def main():
  helpers.init(__file__)
  failures = False
  for i, case in enumerate(test_cases):
    try:
      test(i, case["input"], case["solution"])
    except AssertionError as ae:
      failures = True
      print(ae)
  if failures:
    exit()
  solution = solve(read_input())
  helpers.submit(__file__, solution)

def read_input() -> list[str]:
  folder = helpers.get_day_folder((__file__))
  f = open(f'{folder}/input.txt', 'r')
  return f.read().splitlines()

def listify_test_input(test_input: str) -> list[str]:
  return test_input.split()

def solve(inp: list[str]) -> int:
  res = 0
  # Write solution here
  return res

def test(i: int, test_input: str, test_solution: int):
  clean_input = listify_test_input(test_input)
  my_solution = solve(clean_input)
  try:
    assert test_solution == my_solution, f"{FAIL}Case {i}: expected {test_solution} but got {my_solution}{ENDC}"
    print(f"{OKGREEN}Case {i} passed successfully{ENDC}")
  except AssertionError as ae:
    raise(ae)


if __name__ == "__main__":
  main()