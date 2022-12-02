import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """A Y
B X
C Z""",
"solution": 15
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    for pair in inp:
      split = pair.split(' ')
      first, second = split[0], split[1]
      if second == "X":
        res += 1
        if first == "A":
          res += 3
        elif first == "C":
          res += 6
        
      elif second == "Y":
        res += 2
        if first == "A":
          res += 6
        elif first == "B":
          res += 3

      elif second == "Z":
        res += 3
        if first == "B":
          res += 6
        elif first == "C":
          res += 3

    return res
    

if __name__ == "__main__":
  main()