import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": 
"""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""",
"solution": 13
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    t_loc, h_loc = [0, 0], [0, 0]
    t_visited = set()
    t_visited.add((0,0))
    for command in inp:
      direction, count = command.split(" ")
      count = int(count)
      for _ in range(count):
        if direction == "U":
          h_loc[1] += 1
        elif direction == "D":
          h_loc[1] -= 1
        elif direction == "L":
          h_loc[0] -= 1
        elif direction == "R":
          h_loc[0] += 1
        t_loc = self.t_catchup(t_loc, h_loc)
        t_visited.add(tuple(t_loc))
    return len(t_visited)

if __name__ == "__main__":
  main()