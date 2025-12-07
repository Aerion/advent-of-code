#!/usr/bin/env python

from aocd import puzzle, submit
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import timedelta
from functools import cache
from rich import print
from sys import stderr
from typing import Optional
import time

EXAMPLE_IDX = None
_start_time = time.time()

data = (puzzle.examples[EXAMPLE_IDX] if EXAMPLE_IDX is not None else puzzle).input_data
if EXAMPLE_IDX == 0:
    # Override data if needed
    # data = """REPLACE_ME"""
    pass

print(f"Puzzle #{puzzle.day}", file=stderr)

if EXAMPLE_IDX is not None:
    print(f"Using example #{EXAMPLE_IDX} data", file=stderr)
else:
    print(f"Using PROD data", file=stderr)

#################################################################
# No changes before this line
#################################################################

grid = [[x for x in line] for line in data.splitlines()]
R = len(grid)
C = len(grid[0])

def is_valid(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[r])

beam_pos = grid[0].index('S')

possibilities_count: dict[tuple[int, int], int] = {}

def explore(r, c):
    if not is_valid(r, c):
        return 0

    if (r, c) in possibilities_count:
        return possibilities_count[(r, c)]

    if r == R - 1:
        # end
        return 1
    if grid[r][c] == "." or grid[r][c] == "S":
        possibilities = explore(r + 1, c)
    elif grid[r][c] == "^":
        possibilities = explore(r, c + 1) + explore(r, c - 1)
    else:
        print(grid[r][c])
        assert False
    possibilities_count[(r, c)] = possibilities
    return possibilities

explore(0, beam_pos)
result = possibilities_count[(0, beam_pos)]

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)