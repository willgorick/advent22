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
]

class Wind:
  def __init__(self, x, y, deltas, width, height):
    self.x = x
    self.y = y
    self.dx = deltas[0]
    self.dy = deltas[1]
    self.width = width
    self.height = height
  def __repr__(self):
    return f"{self.x}, {self.y}, {self.dx}, {self.dy}"
      
  def move(self):
    self.x=(self.x+self.dx)%self.width
    self.y=(self.y+self.dy)%self.height

def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    lines = [line for line in inp]
    deltas_from_char = {'v': (0,1), '^': (0,-1), '>': (1,0), '<': (-1,0)}

    self.width = len(lines[0]) - 2
    self.height = len(lines) - 2
    self.dirs = [(1,0), (0,1), (0,-1), (-1, 0), (0, 0)]

    start = (0, -1)
    end = (self.width-1, self.height)

    self.winds = [Wind(x, y, deltas_from_char[char], self.width, self.height) for y, line in enumerate(lines[1:-1]) for x, char in enumerate(line[1:-1]) if char != '.']

    a = self.bfs(start,end)
    print(f"Part 1: {a}")

    b = self.bfs(end, start)
    c = self.bfs(start, end)

    print(f"Part 2: {a+b+c}")

  def bfs(self, start, goal):
    tokens = {start}
    steps = 0

    while goal not in tokens:
      steps += 1
      next_tokens = set()
      for token in tokens:
        next_tokens.add(token)
        for dx, dy in self.dirs: #basically get every potential move & the current loc
          nx = token[0] + dx
          ny = token[1] + dy
          if (0 <= ny < self.height and 0 <= nx < self.width) or (nx, ny) == goal: #add it to our next tokens if it's inbounds or our goals
            next_tokens.add((nx,ny))

      #move all winds, remove any potential moves that overlap with the wind
      for wind in self.winds:
        wind.move()
        next_tokens.discard((wind.x,wind.y))
      tokens = next_tokens
    return steps

if __name__ == "__main__":
  main()