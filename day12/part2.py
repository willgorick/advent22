import sys
import os.path
from heapq import *

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""",
"solution": 29
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    starts = []
    for i in range(len(inp)):
      inp_line = inp[i]
      inp[i] = []
      inp[i][:0] = inp_line

    for i in range(len(inp)):
      for j in range(len(inp[i])):
        if inp[i][j] == "S" or inp[i][j] == "a":
          starts.append([i, j])
    self.inp = inp
    res_list = []
    for start in starts:
      self.visited = set(start)
      self.bfs_queue = []
      heappush(self.bfs_queue, (0, start))
      while self.bfs_queue:
        count, idx = heappop(self.bfs_queue)
        potential_res = self.bfs(count, idx)

        if potential_res != None:
          res_list.append(potential_res)
    print(min(res_list))
    return min(res_list)
  
  def bfs(self, count: int, idx: list[int]):
    curr_x = idx[0]
    curr_y = idx[1]
    curr_ord = ord(self.inp[curr_x][curr_y])
    if curr_ord == 83: #on start idx
      curr_ord = 96 #reset to 1 below 'a'
    for (x, y) in self.dirs:
      new_x = curr_x + x
      new_y = curr_y + y
      if all(
        [new_x >= 0, new_x < len(self.inp), new_y >= 0, new_y < len(self.inp[0]), (new_x, new_y) not in self.visited]
        ): #valid coordinate on the grid
        new_ord = ord(self.inp[new_x][new_y])
        if new_ord == 69:
          if curr_ord >= 121: #if we can reach E and we're at y or z
            return count + 1
        elif new_ord == 83:
          continue
        else: 
          if new_ord <= curr_ord + 1: #1 above or less, add it to the queue with an incremented count
            heappush(self.bfs_queue, (count+1, [new_x, new_y]))
            self.visited.add((new_x, new_y))
    return None




if __name__ == "__main__":
  main()