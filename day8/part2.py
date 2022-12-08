import sys
import os.path

REPO = os.path.dirname(os.path.dirname(__file__))
sys.path.append(REPO)
sys.path.append(f'{REPO}/util')

from solution import Solution

TEST_CASES = [
{
"input": """30373
25512
65332
33549
35390""",
"solution": 8
}
]
  
def main():
  solution = PartSolution(__file__, sys.argv)
  solution.test_cases = TEST_CASES
  solution.run()
  
class PartSolution(Solution):
  def solve(self, inp, test=False):
    def scenic_score(i:int, j:int):
      score_left, score_right, score_up, score_down = 0, 0, 0, 0
      view = inp[i][j]
      i_up, i_down = i-1, i+1
      j_left, j_right = j-1, j+1

      while i_up >= 0:
        check = inp[i_up][j]
        score_up += 1
        if check >= view:
          break
        i_up -= 1

      while i_down < len(inp):
        check = inp[i_down][j]
        score_down += 1
        if check >= view:
          break
        i_down += 1
      
      while j_left >= 0:
        check = inp[i][j_left]
        score_left += 1
        if check >= view:
          break
        j_left -= 1

      while j_right < len(inp[i]):
        check = inp[i][j_right]
        score_right += 1
        if check >= view:
          break
        j_right += 1

      res = score_up * score_left * score_down * score_right

      return res

    res = 0
    for i in range(len(inp)):
      for j in range(len(inp[i])):
        res = max(res, scenic_score(i, j))
    return res
    

if __name__ == "__main__":
  main()