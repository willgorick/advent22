from collections import defaultdict
import sys
import os.path
import re

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""",
"solution": 56000011
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    self.impossible = defaultdict(set)
    self.check_set = set()

    if test:
      check_y = 20
    else:
      check_y = 4000000

    for line in inp:
      print(line)
      m = re.match(r"Sensor at x=(-?[0-9]*), y=(-?[0-9]*): closest beacon is at x=(-?[0-9]*), y=(-?[0-9]*)", line)
      sensor = (int(m.group(1)), int(m.group(2)))
      beacon = (int(m.group(3)), int(m.group(4)))
      dist = self.calculate_manhattan(sensor, beacon)

      for y in range(max(0, sensor[1]-dist), min(sensor[1]+dist+1, check_y+1)):
        check_dist = abs(sensor[1]-y) #get how far away it is
        width = dist-check_dist
        self.impossible[y].add((max(sensor[0]-width, 0), min(sensor[0]+width, check_y)))

    res = 4000000
    for i in range(check_y):
      possible_res = self.merge_intervals(self.impossible[i], i)
      if possible_res != -1:
        return res * possible_res[1] + possible_res[0]
  
  def merge_intervals(self, intervals: set, y: int):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    total_interval = [sorted_intervals[0][0], sorted_intervals[0][1]]
    for i in range(1, len(intervals)):
      # allow merging intervals if they're off by 1 i.e., [0,3] and [4-6] 
      # should be merged because all numbers [0-6] cannot be beacon locations
      if sorted_intervals[i][0] - 1 > total_interval[1]: 
        return (y, sorted_intervals[i][0] - 1)
      else:
        total_interval[0] = min(sorted_intervals[i][0], total_interval[0])
        total_interval[1] = max(sorted_intervals[i][1], total_interval[1])
    return -1

  def calculate_manhattan(self, sensor: tuple, beacon: tuple):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

if __name__ == "__main__":
  main()