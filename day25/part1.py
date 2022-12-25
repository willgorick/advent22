import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""",
"solution": "2=-1=0"
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):

    self.snafu_to_dec_map = {
      "=": -2,
      "-": -1,
      "0": 0,
      "1": 1,
      "2": 2
    }

    self.dec_to_snafu_map = {
      -2: "=",
      -1: "-",
      0: "0",
      1: "1",
      2: "2"
    }

    dec_sum = sum([self.snafu_to_decimal(line) for line in inp])

    snafu_sum = self.decimal_to_snafu(dec_sum)
    print(snafu_sum)
    return snafu_sum

  def snafu_to_decimal(self, snafu: str) -> int:
    res = 0
    for i in range(len(snafu)):
      res += self.snafu_to_dec_map[snafu[len(snafu)-i-1]] * pow(5, i)
    return res

  def decimal_to_snafu(self, dec: int) -> str:
    snafu = []
    while dec > 0:
      remainder = dec % 5
      if remainder >= 3:
        dec += remainder
        snafu.append(self.dec_to_snafu_map[remainder-5])
      else:
        snafu.append(self.dec_to_snafu_map[remainder])
      dec //= 5

    return "".join(reversed(snafu))
if __name__ == "__main__":
  main()