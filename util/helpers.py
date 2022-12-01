import os.path
import requests
import re

class Helper:
  def __init__(self, f: str, args: list[str]):
    self.file = f
    self.folder = self.get_day_folder()
    self.day = self._get_day()
    self.part = self._get_part()
    self.local_input_file = f'{self.folder}/files/input.txt'
    self.local_problem_file = f'{self.folder}/files/problem{self.part}.html'
    self.local_answers_file = f'{self.folder}/files/answer{self.part}.txt'
    self.cookies = {'Cookie': f'session={os.getenv("session")}'}
    self.refresh = False
    self.lite = False
    self.download = False
    self.dry = False
    self.parse_args(args)
    self.year = 2022

    #codes for coloring/styling printed output
    self.OKGREEN = '\033[92m'
    self.BOLD = '\033[1m'
    self.ENDC = '\033[0m'
    self.FAIL = '\033[91m'

    #regex for parsing the response from hitting the /answer endpoint
    self.TOO_QUICK = re.compile('You gave an answer too recently.*to wait.')
    self.WRONG = re.compile(r"That's not the right answer.*?\.")
    self.RIGHT = "That's the right answer!"
    self.ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")

    if not os.path.exists(self.local_input_file):
      self._fetch_and_write_input()
    else:
      print(f"Input file for day {self.day} already downloaded")

    if not self.lite and (not os.path.exists(self.local_problem_file) or self.refresh):
      self._fetch_and_write_problem()
    elif self.lite:
      print(f'Skipping download of problem file for day {self.day} because SPEED')
    else:
      print(f"Problem file for day {self.day} already downloaded")

  def get_day_folder(self) -> str:
    return os.path.dirname(self.file)

  def _get_input(self) -> str:
    url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
    try:
      response = requests.get(url, headers=self.cookies)
    except:
      raise Exception("Unknown error encountered downloading the input file")
    if response.status_code >= 400:
      raise Exception("400 Error encountered downloading the input file")
    return response.text.strip()

  def _get_problem(self) -> str:
    url = f'https://adventofcode.com/{self.year}/day/{self.day}'
    try:
      response = requests.get(url, headers=self.cookies)
    except:
      raise Exception("Unknown error encountered downloading the problem file")
    if response.status_code >= 400:
      raise Exception("400 Error encountered downloading the problem file")
    return response.text.strip()

  def _post_solution(self, answer: int) -> str:
    url = f"https://adventofcode.com/{self.year}/day/{self.day}/answer"
    params = {'level': self.part, 'answer': answer}
    resp = requests.post(url, data=params, headers=self.cookies)
    return resp.text

  def _get_day(self):
    day_s = os.path.basename(self.folder)
    return int(day_s[3:])

  def _get_part(self) -> str:
    curr_file = os.path.basename(self.file)
    return curr_file[4:-3]

  def _fetch_and_write_problem(self) -> None:
    print(f"{'Refresh requested: D' if self.refresh else 'D'}ownloading the problem file for day {self.day}")
    try:
      problem = self._get_problem()
      os.makedirs(os.path.dirname(self.local_problem_file), exist_ok=True)
      with open(self.local_problem_file, 'w') as problem_file:
        problem_file.write(problem)
        #add the stylesheet for live preview in your code editor of choice
        problem_file.write(f'<link rel="stylesheet" type="text/css" href="https://adventofcode.com/static/style.css?30"></script>')
    except Exception as e:
        print(e)
        exit()

  def _fetch_and_write_input(self) -> None:
    print(f"Downloading input file for day {self.day}")
    try:
      s = self._get_input()
      os.makedirs(os.path.dirname(self.local_input_file), exist_ok=True)
      with open(self.local_input_file, 'w') as input_file:
        input_file.write(s)
    except Exception as e:
      print(e)
      exit()

  def parse_args(self, args: list[str]) -> None:
    if "refresh" in args:
      self.refresh = True
    if "lite" in args:
      self.lite = True
    if "download" in args:
      self.download = True
    if "dry" in args:
      self.dry = True
    
  def submit(self, answer: int):
    if self.dry:
      with open(self.local_answers_file, 'a') as answers_file:
          answers_file.write(f'DRY: {str(answer)}\n')
      exit()
    response = self._post_solution(answer=answer)
    for error_regex in (self.WRONG, self.TOO_QUICK, self.ALREADY_DONE):
      error_match = error_regex.search(response)
      if error_match:
        print(f'\n{self.BOLD}{self.FAIL}{error_match[0]}{self.ENDC}{self.ENDC}')
        with open(self.local_answers_file, 'a') as answers_file:
          answers_file.write(f'WRONG: {str(answer)}\n')
        return

    if self.RIGHT in response:
      print(f'\n{self.BOLD}{self.OKGREEN}{self.RIGHT}{self.ENDC}{self.ENDC}')
      with open(self.local_answers_file, 'a') as answers_file:
          answers_file.write(f'RIGHT: {str(answer)}\n')
      return
    else:
      print(f'\n{response}')
      return