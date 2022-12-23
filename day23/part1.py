import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input":
"""..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............""",
"solution": 110
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    DEBUG = "debug" in sys.argv

    #coords to check for each direction
    self.check_map = {
      0: [(-1, -1), (-1, 0), (-1, 1)], #N
      1: [(1, -1), (1, 0), (1, 1)],    #S
      2: [(-1, -1), (0, -1), (1, -1)], #W
      3: [(-1, 1), (0, 1), (1, 1)]     #E
    }

    #where to move elf, if the check_map is all open
    self.dir_map = {
      0: (-1, 0), #N
      1: (1, 0),  #S
      2: (0, -1), #W
      3: (0, 1),  #E
    }
    self.coord_set = set()
    for i in range(len(inp)):
      for j in range(len(inp[i])):
        if inp[i][j] == "#":
          self.coord_set.add((i,j))

    if DEBUG:
      for i in range(12):
        line = ""
        for j in range(14):
          if (i,j) in self.coord_set:
            line += "#"
          else:
            line += "."
        print(line)
      print()

    start_dir = 0
    for _ in range(10):
      #map of potential new coords to their original coords
      potential_moves = {}
      duplicate_moves = set()
      for coord in self.coord_set:
        if DEBUG:
          print(f"COORD: {coord}")
        if self.none_around(coord):
          if DEBUG:
            print(f"COORD: {coord} doesn't need to move")
          continue
        i = 0
        curr_dir = start_dir
        while i < 4:
          if DEBUG:
            print(f"Trying: {curr_dir}")
          curr_dir_moveable = True
          for check in self.check_map[curr_dir]:
            check_spot = (coord[0]+check[0], coord[1]+check[1])
            if DEBUG:
              print(check_spot)
            if check_spot in self.coord_set:
              curr_dir_moveable = False
          #nothing blocking us from moving in this direction
          if curr_dir_moveable:
            if DEBUG:
              print(f"{curr_dir} is moveable")
            #someone else has already tried to move here
            relative_move = self.dir_map[curr_dir]
            potential_move = (coord[0]+relative_move[0], coord[1]+relative_move[1])
            if potential_move in potential_moves:
              duplicate_moves.add(potential_move)
            #nobody has tried to move here before, so map this new location to the current coord
            else:
              potential_moves[potential_move] = coord
            #break out of the while loop
            break
          #we cannot move in that direction
          else:
            i += 1
            curr_dir = self.next_dir(curr_dir)
      #update all coords that could move and don't overlap
      for move, origin in potential_moves.items():
        #don't move if multiple people want to move there
        if move in duplicate_moves:
          continue
        else:
          self.coord_set.remove(origin)
          self.coord_set.add(move)
      #update the start direction
      start_dir = self.next_dir(start_dir)
    
    if DEBUG:
      for i in range(12):
        line = ""
        for j in range(14):
          if (i,j) in self.coord_set:
            line += "#"
          else:
            line += "."
        print(line)
    min_i, min_j = float("inf"), float("inf")
    max_i, max_j = -float("inf"), -float("inf")
    for coord in self.coord_set:
      max_i = max(coord[0], max_i)
      min_i = min(coord[0], min_i)
      max_j = max(coord[1], max_j)
      min_j = min(coord[1], min_j)

    rect_size = (max_i+1 - min_i) * (max_j+1 - min_j)
    return rect_size - len(self.coord_set)
  
  def next_dir(self, curr_dir):
    return (curr_dir+1) % 4

  def none_around(self, coord):
    surrounding = set([(coord[0]+i,coord[1]+j) for i in [-1, 0, 1] for j in [-1, 0, 1]])
    surrounding.remove(coord)
    for possible in surrounding:
      if possible in self.coord_set:
        return False
    return True

if __name__ == "__main__":
  main()