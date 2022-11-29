import os.path
import requests
import sys
import re

CWD = os.getcwd()
TOO_QUICK = re.compile('You gave an answer too recently.*to wait.')
WRONG = re.compile(r"That's not the right answer.*?\.")
RIGHT = "That's the right answer!"
ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")

def _get_cookie_value() -> dict[str, str]:
  with open(os.path.join(os.path.dirname(CWD), '.env')) as f:
    contents = f.read().strip()
  return {'Cookie': contents}


def get_input(day: int, year: int) -> str:
  cookies = _get_cookie_value()
  url = f'https://adventofcode.com/{year}/day/{day}/input'
  try:
    response = requests.get(url, headers=cookies)
  except:
    raise Exception("Unknown error encountered downloading the input file")
  if response.status_code >= 400:
    raise Exception("400 Error encountered downloading the input file")
  return response.text.strip()


def submit(answer: int):
  response = _post_solution(answer, _get_cookie_value(), _get_part(), _get_day(), 2021)
  for error_regex in (WRONG, TOO_QUICK, ALREADY_DONE):
    error_match = error_regex.search(response)
    if error_match:
      print(f'\033[91m{error_match[0]}\033[m')
      return

  if RIGHT in response:
    print(f'\033[92m{RIGHT}\033[m')
    return
  else:
    print(response)
    return

def _post_solution(answer: int, cookies: dict[str, str], part: int, day: int, year: int) -> str:
  url = f"https://adventofcode.com/{year}/day/{day}/answer"
  params = {'level': part, 'answer': answer}
  resp = requests.post(url, data=params, headers=cookies)
  return resp.text

def _get_day():
  day_s = os.path.basename(CWD)
  return int(day_s[3:])


def _get_part():
  curr_file = sys.argv[0]
  return curr_file[4:-3]

def init():
  day = _get_day()
  if not os.path.exists('./input.txt'):
    print(f"downloading input file for day {day}")
    try:
      s = get_input(day, 2021)
      with open('input.txt', 'w') as f:
        f.write(s)
    except Exception as e:
      print(e)
      exit()
  else:
    print(f"input file for day {day} already downloaded")
  
