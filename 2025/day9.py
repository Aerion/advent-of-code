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
    r, c = line.split(",")
    positions.append((int(r), int(c)))

example_values = {
    (2,5, 9,7): 24,
    (7,1, 11,7): 35,
    (7, 3, 2, 3): 6,
    (2, 5, 7, 11): 50,
}

max_area = 0
for i in range(len(positions)):
    for j in range(len(positions)):
        if i == j:
            continue
        x_distance = abs(positions[i][0] - positions[j][0]) + 1
        y_distance = abs(positions[i][1] - positions[j][1]) + 1
        area = abs(x_distance * y_distance)

        """
        example_result = example_values.get((*positions[i], *positions[j]))
        if example_result:
            print(x_distance, y_distance, positions[i], positions[j])
            assert area == example_result
        """

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