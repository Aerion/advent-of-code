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

@dataclass
class Range:
    low: int
    high: int

def parse_input():
    is_range = True
    ranges = []
    ids = []
    for line in data.splitlines():
        if not line:
            is_range = False
            continue
        if is_range:
            low, high = [int(x) for x in line.split("-")]
            ranges.append(Range(low, high))
            continue
        ids.append(int(line))
    return ranges, ids

def simplify_ranges(ranges: list[Range]):
    output: list[Range] = []
    for candidate_range in sorted(ranges, key=lambda range: range.low):
        if not output:
            output.append(candidate_range)
            continue
        if candidate_range.low <= output[-1].high:
            # The latest range can still be extended
            output[-1].high = max(candidate_range.high, output[-1].high)
            continue

        # No overlap with the existing one
        output.append(candidate_range)

    return output

ranges, ids = parse_input()
ranges = simplify_ranges(ranges)
print(ranges)

result = 0
for range in ranges:
    result += range.high - range.low + 1

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)