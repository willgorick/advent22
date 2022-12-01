from helpers import Helper
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())   

class Solution:
  def __init__(self, f: str, args: list[str]):
    self.file = f
    self.args = args
    self.helper = Helper(self.file, self.args)
    self.input = self.read_input()
    if len(self.input) == 1:
      self.input = self.comma_split_input(self.input[0])
    self.test_cases = []
    self.failures = False
    
  def run(self):
    if self.helper.download:
      print(self.input)
      exit()
    for i in range(len(self.test_cases)):
      try:
        self.test(i)
      except AssertionError as ae:
        self.failures = True
        print(ae)
    if self.failures:
      exit()
    solution = self.solve(self.input)
    self.helper.submit(solution)

  def set_test_cases(self, test_cases: list[dict[str, str]]):
    self.test_cases = test_cases

  def read_input(self) -> list[str]:
    f = open(f'{self.helper.local_input_file}')
    return f.read().splitlines()

  def newline_split_input(self, test_input: str) -> list[str]:
    return test_input.split("\n")

  def comma_split_input(self, inp: str) -> list[str]:
    return inp.split(',')

  def solve(self, inp, test=False) -> int:
    res = 0
    #Write your own solve function!
    return res

  def test(self, i: int):
    clean_input = self.newline_split_input(self.test_cases[i]["input"])
    if len(clean_input) == 1:
      clean_input = self.comma_split_input(clean_input[0])
    my_solution = self.solve(clean_input, test=True)
    test_solution = self.test_cases[i]["solution"]
    try:
      assert test_solution == my_solution, f"{self.helper.FAIL}Case {i}: expected {test_solution} but got {my_solution}{self.helper.ENDC}"
      print(f"{self.helper.OKGREEN}Case {i} passed successfully{self.helper.ENDC}")
    except AssertionError as ae:
      raise(ae)