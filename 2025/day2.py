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
    #data = """12121212-12341238"""
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
for line in data.split(","):
    first_id, last_id = [int(x) for x in line.split("-")]
    for i in range(first_id, last_id + 1):
        if i < 10:
            continue
        s = str(i)
        # Only handle prime ones
        # 1 time
        if len(set(s)) == 1:
            result += i
            print(i)
            continue
        
        for prime in [2, 3, 5, 7, 9, 11, 13, 17, 19]:
            if len(s) % prime != 0:
                continue
            slices = set()
            len_slice = len(s) // prime
            for idx in range(prime):
                low = idx * len_slice
                high = (idx + 1) * len_slice
                slices.add(s[low:high])
            if len(slices) == 1:
                print(i, prime)
                result += i
                break

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)