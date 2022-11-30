import os.path
import requests
import sys
import re

CWD = os.getcwd()

#regex for parsing the response from hitting the /answer endpoint
TOO_QUICK = re.compile('You gave an answer too recently.*to wait.')
WRONG = re.compile(r"That's not the right answer.*?\.")
RIGHT = "That's the right answer!"
ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")

#codes for coloring/styling printed output
OKGREEN = '\033[92m'
BOLD = '\033[1m'
ENDC = '\033[0m'
FAIL = '\033[91m'

def _get_cookie_value(f: str) -> dict[str, str]:
  try:
    with open(os.path.join(os.path.dirname(get_day_folder(f)), '.env')) as env:
      contents = env.read().strip()
  except Exception as e:
    raise e
  return {'Cookie': contents}

def get_day_folder(f: str) -> str:
  return os.path.dirname(f)

def _get_input(f: str, day: int, year: int) -> str:
  try:
    cookies = _get_cookie_value(f)
  except Exception as e:
    raise e
  url = f'https://adventofcode.com/{year}/day/{day}/input'
  try:
    response = requests.get(url, headers=cookies)
  except:
    raise Exception("Unknown error encountered downloading the input file")
  if response.status_code >= 400:
    raise Exception("400 Error encountered downloading the input file")
  return response.text.strip()

def _get_problem(f: str, day:int, year: int) -> str:
  try:
    cookies = _get_cookie_value(f)
  except Exception as e:
    raise e
  url = f'https://adventofcode.com/{year}/day/{day}'
  try:
    response = requests.get(url, headers=cookies)
  except:
    raise Exception("Unknown error encountered downloading the problem file")
  if response.status_code >= 400:
    raise Exception("400 Error encountered downloading the problem file")
  return response.text.strip()

def _post_solution(answer: int, cookies: dict[str, str], part: int, day: int, year: int) -> str:
  url = f"https://adventofcode.com/{year}/day/{day}/answer"
  params = {'level': part, 'answer': answer}
  resp = requests.post(url, data=params, headers=cookies)
  return resp.text

def _get_day(f: str):
  day_s = os.path.basename(get_day_folder(f))
  return int(day_s[3:])

def _get_part(f: str):
  curr_file = os.path.basename(f)
  return int(curr_file[4:-3])

def init(f: str):
  day = _get_day(f)
  folder = get_day_folder(f)
  part = _get_part(f)
  if not os.path.exists(os.path.join(folder, 'input.txt')):
    print(f"downloading input file for day {day}")
    try:
      s = _get_input(f, day, 2022)
      with open(os.path.join(folder, 'input.txt'), 'w') as input_file:
        input_file.write(s)
    except Exception as e:
      print(e)
      exit()
  else:
    print(f"input file for day {day} already downloaded")

  if not os.path.exists(os.path.join(folder, f'problem{part}.html')):
    print(f"downloading the problem file for day {day} part {part}")
    try:
      s = _get_problem(f, day, 2022)
      with open(os.path.join(folder, f'problem{part}.html'), 'w') as problem_file:
        problem_file.write(s)
        #add the stylesheet for live preview in your code editor of choice
        problem_file.write(f'<link rel="stylesheet" type="text/css" href="https://adventofcode.com/static/style.css?30"></script>')
    except Exception as e:
      print(e)
      exit()
  else:
    print(f"problem file for day {day} already downloaded")
  
def submit(f: str, answer: int):
  try:
    cookies = _get_cookie_value(f)
  except Exception as e:
    raise e
  response = _post_solution(answer, cookies, _get_part(f), _get_day(f), 2022)
  for error_regex in (WRONG, TOO_QUICK, ALREADY_DONE):
    error_match = error_regex.search(response)
    if error_match:
      print(f'\n{BOLD}{FAIL}{error_match[0]}{ENDC}{ENDC}')
      return

  if RIGHT in response:
    print(f'\n{BOLD}{OKGREEN}{RIGHT}{ENDC}{ENDC}')
    return
  else:
    print(f'\n{response}')
    return