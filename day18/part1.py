import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""",
"solution": 64
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    res = 0
    cube_set = set()
    for line in inp:
      x,y,z = line.split(',')
      cube_set.add((int(x), int(y), int(z)))
    print(cube_set)
    for cube in cube_set:
      x, y, z = cube
      if (x+1, y, z) not in cube_set:
        res += 1
      if (x-1, y, z) not in cube_set:
        res += 1
      if (x, y+1, z) not in cube_set:
        res += 1
      if (x, y-1, z) not in cube_set:
        res += 1
      if (x, y, z+1) not in cube_set:
        res += 1
      if (x, y, z-1) not in cube_set:
        res += 1
    return res
    

if __name__ == "__main__":
  main()