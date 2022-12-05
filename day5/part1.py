import sys
import os.path
from collections import deque

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""",
"solution": 'CMZ'
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    i = 0
    map_stack = {}
    while inp[i] != '':
      for j in range(0, len(inp[i]), 4):
        ind = j//4 + 1
        curr = inp[i][j:j+4]
        curr = ''.join(curr)
        curr = curr.strip().replace('[', '').replace(']', '')
        if curr and not curr.isnumeric():
          if not map_stack.get(ind):
            map_stack[ind] = deque([curr])
          else:
            map_stack[ind].append(curr.strip().replace('[', '').replace(']', ''))
      i += 1

    res = []
    for i in range(i+1, len(inp), 1):
      command_list = inp[i].split(' ')
      count, source, destination = int(command_list[1]), int(command_list[3]), int(command_list[5])
      for i in range(count):
        map_stack[destination].appendleft(map_stack[source].popleft())
    for i in range(1, len(map_stack)+1):
      res.append(map_stack[i][0])
    return ''.join(res)
    

if __name__ == "__main__":
  main()