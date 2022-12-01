<b>Howdy!  Welcome to my 2022 Advent of Code repository!</b>

In order to run your code in this repo, you will need to add a .env file with your session cookie from the advent of code site.  To access this, login to your account at https://adventofcode.com/ and inspect the page, then grab the `session` cookie (this process will be slightly different depending on your browser).  Once you've acquired the cookie, save it in your .env file in the format `session={cookie}`

In order to start actually working, you can copy the `day0` folder, modifying the name to a new `day{number}` folder and simply add your solution to the `solve()` function inside the part1.py file.

By default, as long as the helpers.init() function is called and your folder and file name conventions match mine, the input file will be automatically downloaded, as well as the raw html of the problem page, in case you want to view it using your IDE's live preview extension.  These files will be found in the `files/` folder within the day you're working on.  If for any reason you want to refresh the files (such as when you've solved part1 and want to read part2), you can do so by adding the "refresh" command line argument.  Alternatively, if you're interested in a more minimal experience, you can add "lite" as a command line argument and skip downloading the problem html.

As you may have noticed from the command above, this repository uses Python3.  Attempting to run it with older Python will not work.