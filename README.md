# Advent of Code 2019
I will publish my solutions for [Advent of Code](https://adventofcode.com/2019) puzzles here.
Main implementation language will be Python 3.

The puzzle inputs for each day are stored in folder _input_.
The solutions are written to folder _output_.
Each programming language has it's own folder for implementation (currently only Python).

# Python
The class _AOC_ in _aoc.py_ implements some general functionality and can be used in the specific implementations.
It will also create (based on the template _day00.py_) a script for each day with basic implementation (getting input, save results, ...).
The daily puzzle input will be fetched from [adventofcode.com](https://adventofcode.com/2019) and saved to the corresponding file in _input_.
Therefor credentials (cookies) are stored in file _cookies.txt_ to authenticate to Advent of Code and get personal puzzle input.
The content of the file _cookies.txt_ in main directory looks like this:
```
session=5485cc9b3365b4305dfb4e8337e0a598a574f8242bf17289e0dd6c20a3cd44a089de16ab4ab308f63e44b1170eb5f515
```

# Leaderboard
In folder _python_ you will find _\_leaderbord.py_ which is a little script to display your local leaderbord.
It displays the time everyone needed to solve the tasks (strictly speaking, it shows the time; time zone UTC+1).

It will fetch all data from [adventofcode.com](https://adventofcode.com) and create a local HTML file which is then opened in your browser.

You need to provide the desired year and the user ID of the leaderboard owner (you see this at the end of the url of the leaderboard) in _leaderboard.txt_ (in main directory):
```
2019
420690
```

You may are also interested in:\
https://addons.mozilla.org/en-US/firefox/addon/aoc-ranking/ \
https://addons.mozilla.org/en-US/firefox/addon/advent-of-code-charts/