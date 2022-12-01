import sys
import os.path
#add helpers file to sys.path
REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
from util import helpers

def main():
  helper = helpers.Helper(__file__, sys.argv)
  solution = Solution(helper)

class Solution:
  def __init__(self, helper: helpers.Helper):
    self.helper = helper
    self.input = self.read_input()
    self.test_cases = [
      {
        "input": """
          199
          200
          208
          210
          200
          207
          240
          269
          260
          263
        """,
        "solution": 7
      },
      {
        "input": """
        """,
        "solution": 0
      }
    ]
  
    self.failures = False
    for i in range(len(self.test_cases)):
      try:
        self.test(i)
      except AssertionError as ae:
        self.failures = True
        print(ae)
    if self.failures:
      exit()
    solution = self.solve(self.input)
    helper.submit(solution)


  def read_input(self) -> list[str]:
    f = open(f'{self.helper.local_input_file}')
    return f.read().splitlines()

  def listify_test_input(self, test_input: str) -> list[str]:
    return test_input.split()

  def solve(self, inp) -> int:
    res = 0
    for i in range(len(inp)):
      if i != 0 and int(inp[i]) > int(inp[i-1]):
        res += 1
    return res

  def test(self, i: int):
    clean_input = self.listify_test_input(self.test_cases[i]["input"])
    my_solution = self.solve(clean_input)
    test_solution = self.test_cases[i]["solution"]
    try:
      assert test_solution == my_solution, f"{self.helper.FAIL}Case {i}: expected {test_solution} but got {my_solution}{self.helper.ENDC}"
      print(f"{self.helper.OKGREEN}Case {i} passed successfully{self.helper.ENDC}")
    except AssertionError as ae:
      raise(ae)


if __name__ == "__main__":
  main()