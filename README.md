<b>Howdy!  Welcome to my 2022 Advent of Code repository!</b>

In order to run your code in this repo, just two steps are required:

1. The first is adding a .env file with your session cookie from the advent of code site.  To access this, login to your account at https://adventofcode.com/ and inspect the page, then grab the `session` cookie (this process will be slightly different depending on your browser).  Once you've acquired the cookie, save it in your .env file in the format `session: {cookie}`
2. In order to properly import the needed functions from the util folder, you'll need to run the setup.py script with the command ```python3 setup.py install``` from the top level of this repository.

In order to start actually working, you can copy the `day0` folder, modifying the name to a new `day{number}` folder and simply add your solution to the `solve()` function inside the part1.py file.
As you may have noticed from the command above, this repository uses Python3.  Attempting to run it with older Python will not work.