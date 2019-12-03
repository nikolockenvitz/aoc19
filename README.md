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