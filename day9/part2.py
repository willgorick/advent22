import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution
import tail

TEST_CASES = [
{
"input": 
"""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""",
"solution": 36
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    knot_list = [[0,0] for _ in range(10)]
    t_visited = set()
    t_visited.add((0,0))
    for command in inp:
      direction, count = command.split(" ")
      count = int(count)
      for _ in range(count):
        if direction == "U":
          knot_list[0][1] += 1
        elif direction == "D":
          knot_list[0][1] -= 1
        elif direction == "L":
          knot_list[0][0] -= 1
        elif direction == "R":
          knot_list[0][0] += 1
        for i in range(1, 10):
          knot_list[i] = tail.t_catchup(knot_list[i], knot_list[i-1])
        t_visited.add(tuple(knot_list[9]))
    return len(t_visited)

if __name__ == "__main__":
  main()