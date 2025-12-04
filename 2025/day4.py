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


result = 0
initial_roll_count = 0
for char in data:
    if char == "@":
        initial_roll_count += 1
grid = data.splitlines()

directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]

R = len(grid)
C = len(grid[0])
MAX_ROLLS = 4

def is_roll(r, c, new):
    return 0 <= r < R and 0 <= c < C and (grid[r][c] == '@' or (new and grid[r][c] > 0))

def print_grid():
    for row in grid:
        print("".join((str(x) for x in row)))

new_grid = []
for r in range(R):
    new_grid.append([])
    for c in range(C):
        if not is_roll(r, c, False):
            new_grid[r].append(0)
            continue

        rolls_count = 0
        for direction in directions:
            new_r = direction[0] + r
            new_c = direction[1] + c
            if is_roll(new_r, new_c, False):
                rolls_count += 1

        new_grid[r].append(rolls_count)

grid = new_grid
print_grid()

changed = None
while changed != False:
    changed = False
    for r in range(R):
        for c in range(C):
            if not is_roll(r, c, True):
                continue

            if grid[r][c] < MAX_ROLLS:
                for direction in directions:
                    new_r = direction[0] + r
                    new_c = direction[1] + c
                    if is_roll(new_r, new_c, True):
                        grid[new_r][new_c] -= 1
                grid[r][c] = 0
                changed = True
    print("-------")
print_grid()

roll_count = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] > 0:
            roll_count += 1

result = initial_roll_count - roll_count

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)