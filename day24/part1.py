import sys
import os.path
from collections import defaultdict, deque
import heapq
from time import perf_counter

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": 
"""#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""",
"solution": 18
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    DEBUG = "debug" in sys.argv

    #initialize self.res to inf, then decrease as we find better solutions
    self.res = float("inf")
    
    self.dirs = [(1,0), (0,1), (0,-1), (-1, 0)]

    #initial layout of the field
    initial_field = defaultdict(set)

    #start coordinate
    start = (0, 1)

    #end coordinate
    self.goal = (len(inp)-1, len(inp[0])-2)
    print(f"Goal: {self.goal}")
    #height and width of the field
    self.height, self.width = len(inp), len(inp[0])

    #visited set is a tuple of move and coord
    #ex visited set entry: (2, (1,3))
    self.visited = set()

    for i in range(1, len(inp)-1):
      for j in range(1, len(inp[0])-1):
        if inp[i][j] != ".":
          initial_field[(i,j)].add(inp[i][j])

    if DEBUG:
      for coord, val in initial_field.items():
        print(coord, val)
      print()
    self.heap = []
    heapq.heapify(self.heap)
    m_dist = abs(self.goal[0] - start[0]) + abs(self.goal[1] - start[1])
    heapq.heappush(self.heap, (m_dist, 0, start, initial_field))
    self.visited.add((0, start[0], start[1]))
    self.tic = perf_counter()
    while self.heap:
      m_dist, mins, loc, field = heapq.heappop(self.heap)
      self.bfs(mins, loc, field)

    print(f"uh: {self.res}")
    toc = perf_counter()
    time_diff = toc - self.tic
    if time_diff > 60:
      print(f"took {time_diff // 60} minutes {time_diff % 60} seconds")
    else:
      print(f"took {toc - self.tic:0.6f} seconds")
    return self.res
  
  def bfs(self, mins, my_loc, field):
    # prune the branch if it is impossible for us to get to the goal in less 
    # than the current result time even if we moved optimally every minute
    if mins >= self.res or abs(self.goal[0] - my_loc[0]) + abs(self.goal[1] - my_loc[1]) > self.res - mins:
      return 

    #move the blizzards
    field = self.move_blizzards(field)
 
    #consider moving in each direction
    for d_i, d_j in self.dirs:
      new_i, new_j = my_loc[0] + d_i, my_loc[1] + d_j
      
      # if a candidate move is the end, update res if we 
      # got there faster than previous branches and return
      if self.goal == (new_i, new_j):
        print(mins+1)
        time_diff = perf_counter() - self.tic
        print(f"took {time_diff // 60} minutes {time_diff % 60} seconds")
        self.res = min(self.res, mins+1)
        return
      
      # skip any attempts to move out of bounds
      if any(
        [new_i <= 0, new_i >= self.height-1, new_j <= 0, new_j >= self.width-1]
      ):
        continue 
      
      # don't redo work another branch has already done
      if (mins+1, new_i, new_j) not in self.visited and (new_i, new_j) not in field:
        self.visited.add((mins+1, new_i, new_j))
        m_dist = abs(self.goal[0] - new_i) + abs(self.goal[1] - new_j)
        heapq.heappush(self.heap, (m_dist, mins+1, (new_i, new_j), field))
    
    #wait at current location
    if (mins+1, my_loc[0], my_loc[1]) not in self.visited and my_loc not in field:
      self.visited.add((mins+1, my_loc[0], my_loc[1]))
      m_dist = abs(self.goal[0] - my_loc[0]) + abs(self.goal[1] - my_loc[1])
      heapq.heappush(self.heap, (m_dist, mins+1, my_loc, field))
    
  def manhattan_to_goal(self, my_loc):
    return abs(self.goal[0] - my_loc[0]) + abs(self.goal[1] - my_loc[1]) 
      
  def move_blizzards(self, field):
    updated_field = defaultdict(set)
    for coord in field:
      for val in field[coord]:
        new_i, new_j = coord[0], coord[1]
        #move blizzard based on it's symbol
        if val == "<":
          new_j -= 1
        elif val == ">":
          new_j += 1
        elif val == "^":
          new_i -= 1
        elif val == "v":
          new_i += 1

        #wrap blizzards if needed
        if new_j == 0:
          new_j = self.width-2
        elif new_j == self.width-1:
          new_j = 1
        elif new_i == 0:
          new_i = self.height-2
        elif new_i == self.height-1:
          new_i = 1
        
        #add val to this coord in our field map
        updated_field[(new_i, new_j)].add(val)
    return updated_field

if __name__ == "__main__":
  main()