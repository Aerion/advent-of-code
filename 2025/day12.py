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
def parse_input():
    elts = data.split("\n\n")

    points_per_shape = []
    for shape_lines in elts[:-1]:
        count = 0
        for shape_line in shape_lines.splitlines()[1:]:
            for char in shape_line:
                if char == "#":
                    count += 1

        points_per_shape.append(count)

    problems = []
    for line in elts[-1].splitlines():
        elts = line.split(" ")

        size_elts = elts[0][:-1].split("x")
        width = int(size_elts[0])
        height = int(size_elts[1])

        required_shapes_count = [int(x) for x in elts[1:]]

        problems.append((width, height, required_shapes_count))

    return points_per_shape, problems

result = 0
points_count_per_shape, region_problems = parse_input()
print(points_count_per_shape)
for problem in region_problems:
    print(problem)
    width, height, required_shapes_count = problem

    points_count = 0
    for i, required_count in enumerate(required_shapes_count):
        points_count += points_count_per_shape[i] * required_count

    print(points_count, width * height)
    if width * height < points_count:
        # can never fit
        continue

    # naive and optimistic approach 🤡
    result += 1

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)