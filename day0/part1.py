#TEMPLATE FILE 

import helpers

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
  helpers.init()
  for i, case in enumerate(test_cases):
    test(i, case["input"], case["solution"])
    solution = solve(read_input())
  helpers.submit(solution)

def read_input():
  f = open('./input.txt', 'r')
  return f.read().splitlines()

def listify_test_input(test_input):
  return test_input.split()

def solve(inp):
  res = 0
  # Write solution here
  return res

def test(i, test_input, test_solution):
  clean_input = listify_test_input(test_input)
  my_solution = solve(clean_input)
  try:
    assert test_solution == my_solution, f"{FAIL}case {i}: expected {test_solution} but got {my_solution}{ENDC}"
    print(f"{OKGREEN}Case {i} passed successfully{ENDC}")
  except AssertionError as ae:
    print(ae)


if __name__ == "__main__":
  main()