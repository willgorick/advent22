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
"solution": 26
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    self.check_set = set()
    if test:
      check_y = 10
    else:
      check_y = 2000000

    for line in inp:
      m = re.match(r"Sensor at x=(-?[0-9]*), y=(-?[0-9]*): closest beacon is at x=(-?[0-9]*), y=(-?[0-9]*)", line)
      sensor = (int(m.group(1)), int(m.group(2)))
      beacon = (int(m.group(3)), int(m.group(4)))
      dist = self.calculate_manhattan(sensor, beacon)
      if check_y >= sensor[1]-dist and check_y <= sensor[1]+dist:
        check_dist = abs(sensor[1]-check_y) #get how far away it is
        for x in range(dist-check_dist+1): #dist - how far away it is = how many in each direction can't be beacons
          if (sensor[0]+x, check_y) != beacon and (sensor[0]+x, check_y) != sensor:
            self.check_set.add(sensor[0]+x)
          if (sensor[0]-x, check_y) != beacon and (sensor[0]-x, check_y) != sensor:
            self.check_set.add(sensor[0]-x)


    res = len(self.check_set)
    print(res)
    return res
  
  def calculate_manhattan(self, sensor: tuple, beacon: tuple):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

if __name__ == "__main__":
  main()