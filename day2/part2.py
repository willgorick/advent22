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
"solution": 12
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    #second now represents the outcome we need
    #x = lose
    #y = draw
    #z = win
    # r, p, s = 1, 2, 3
    # l, d, w = 0, 3, 6
    for pair in inp:
      split = pair.split(' ')
      first, second = split[0], split[1]
      if first == "A": #opponent rock
        if second == "X": #scissors to lose
          res += 3
        elif second == "Y": #rock to draw
          res += 4
        elif second == "Z": #paper to win
          res += 8
          
      elif first == "B": #opponent paper
        if second == "X": #rock to lose
          res += 1
        elif second == "Y": #paper to draw
          res += 5
        elif second == "Z": #scissors to win
          res += 9

      elif first == "C": #opponent scissors
        if second == "X": #paper to lose
          res += 2
        elif second == "Y": #scissors to draw
          res += 6
        elif second == "Z": #rock to win
          res += 7
    return res
    

if __name__ == "__main__":
  main()