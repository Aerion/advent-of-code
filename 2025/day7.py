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

def is_valid(r, c, seen):
    return 0 <= r < len(grid) and 0 <= c < len(grid[r]) and (r, c) not in seen

print(grid[0])
beam_pos = grid[0].index('S')

result = 0
seen = set()
split_history = set()

q = deque()
q.append((0, beam_pos))

while q:
    r, c = q.pop()
    if (r, c) in seen:
        continue
    seen.add((r, c))

    if grid[r][c] == "." or grid[r][c] == "S":
        # Continue the beam
        if is_valid(r + 1, c, seen):
            q.append((r + 1, c))
        continue

    assert grid[r][c] == "^"
    # Split the beam
    split = False
    if is_valid(r, c - 1, seen):
        q.append((r, c - 1))
        split = True
    if is_valid(r, c + 1, seen):
        split = True
        q.append((r, c + 1))
    if split:
        split_history.add((r, c))

for r in range(R):
    for c in range(C):
        if (r, c) in split_history:
            print('x', end='')
        elif (r, c) in seen:
            print('|', end='')
        else:
            print('.', end='')
    print()

result = len(split_history)

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)