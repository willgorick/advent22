import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
from solution import Solution
from myopcode import Opcode

TEST_CASES = [
# {
# "input": """3,0,0,0""",
# "solution": 0
# },
# {
# "input": """4,1""",
# "solution": 0
# },
# {
# "input": """1002,4,3,4,33""",
# "solution": 0
# }
]
  
local_tests = [
  "1002",
  "1101",
  "3",
  "4"
]
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    myop = Opcode(inp)
    myop.process()
    return myop.output[-1]

if __name__ == "__main__":
  main()