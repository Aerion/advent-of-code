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
import heapq

EXAMPLE_IDX = 0
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

def get_min_count(target_joltages: list[int], buttons: list[list[int]]):
    q = []
    heapq.heappush(q, (0, [0] * len(target_joltages), []))

    while q:
        initial_distance, initial_joltages, initial_path = heapq.heappop(q)
        #print(f"{initial_distance=} {initial_joltages=} {initial_path=}")

        for button_idx, button in enumerate(buttons):
            path = initial_path + [button_idx]
            joltages = initial_joltages[:]

            too_much = False
            for key in button:
                joltages[key] += 1
                if joltages[key] > target_joltages[key]:
                    too_much = True

            if too_much:
                continue

            distance = sum((target_joltages[i] - joltages[i]) for i in range(len(target_joltages)))
            #print(f"{joltages=} {distance}")

            if distance == 0:
                print(path)
                return len(path)
            heapq.heappush(q, (distance, joltages, path))

result = 0
for line in data.splitlines():
    elts = line.split(" ")
    buttons_list = [[int(i) for i in x[1:-1].split(",")] for x in elts[1:-1]]
    joltages_list = [int(x) for x in elts[-1][1:-1].split(",")]

    print(f"{buttons_list=}")
    print(f"{joltages_list=}")

    min_count = get_min_count(joltages_list, buttons_list)
    print(min_count)
    result += min_count

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)