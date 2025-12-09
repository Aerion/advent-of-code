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
positions = []
for line in data.splitlines():
    c, r = line.split(",")
    positions.append((int(r), int(c)))

example_values = {
    (3, 7, 1, 11): 15,
    (7, 9, 5, 9): 3,
    (5, 9, 3, 2): 24,
}

authorized_points = set()
for i in range(len(positions)):
    prev_r, prev_c = positions[i - 1]
    cur_r, cur_c = positions[i]

    if prev_c == cur_c:
        # Same columns
        for r in range(min(prev_r, cur_r), max(prev_r, cur_r) + 1):
            authorized_points.add((r, cur_c))
    else:
        assert prev_r == cur_r
        # Same rows
        for c in range(min(prev_c, cur_c), max(prev_c, cur_c) + 1):
            authorized_points.add((cur_r, c))

min_r = min(positions, key=lambda pos: pos[0])[0] - 1
max_r = max(positions, key=lambda pos: pos[0])[0] + 1
min_c = min(positions, key=lambda pos: pos[1])[1] - 1
max_c = max(positions, key=lambda pos: pos[1])[1] + 1

min_c_per_row = { r: float('infinity') for r in range(min_r, max_r)}
max_c_per_row = { r: float('-infinity') for r in range(min_r, max_r)}
min_r_per_column = { r: float('infinity') for r in range(min_c, max_c)}
max_r_per_column = { r: float('-infinity') for r in range(min_c, max_c)}

for r, c in authorized_points:
    min_c_per_row[r] = min(min_c_per_row[r], c)
    max_c_per_row[r] = max(max_c_per_row[r], c)
    min_r_per_column[c] = min(min_r_per_column[c], r)
    max_r_per_column[c] = max(max_r_per_column[c], r)

def print_grid():
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r, c) in positions:
                print('O', end='')
            elif (r, c) in authorized_points:
                print('#', end='')
            else:
                print('.', end='')
        print()

#print_grid()

import tqdm
max_area = 0
for i in tqdm.tqdm(range(len(positions))):
    for j in range(len(positions)):
        if i == j:
            continue
        example_result = example_values.get((*positions[i], *positions[j]))
        if EXAMPLE_IDX is None:
            example_result = None

        r_distance = abs(positions[i][0] - positions[j][0]) + 1
        c_distance = abs(positions[i][1] - positions[j][1]) + 1
        area = abs(r_distance * c_distance)

        min_r = min(positions[i][0], positions[j][0])
        max_r = max(positions[i][0], positions[j][0])
        min_c = min(positions[i][1], positions[j][1])
        max_c = max(positions[i][1], positions[j][1])

        discarded = False
        for c in range(min_c, max_c + 1):
            if min_r < min_r_per_column[c] or max_r > max_r_per_column[c]:
                discarded = True
                break
        if example_result:
            assert not discarded
        if discarded:
            continue

        for r in range(min_r, max_r + 1):
            if min_c < min_c_per_row[r] or max_c > max_c_per_row[r]:
                discarded = True
                break
        if example_result:
            assert not discarded
        if discarded:
            continue

        if example_result:
            print(r_distance, c_distance, positions[i], positions[j])
            assert area == example_result

        if area > max_area:
            max_area = area
result = max_area

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)