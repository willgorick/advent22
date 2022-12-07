import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution
from directory import create_dir

TEST_CASES = [
{
"input": """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""",
"solution": 24933642
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()

class PartSolution(Solution):
  def solve(self, inp, test=False):
    total = 70000000
    directory = create_dir(inp)
    used = directory.count_dfs()
    unused = total - used
    goal = 30000000 - unused

    for size in sorted(directory.size_list):
      if size > goal:
        return size

if __name__ == "__main__":
  main()