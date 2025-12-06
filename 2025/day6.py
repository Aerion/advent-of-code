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

lines = data.splitlines()
R = len(lines) - 1
C = len(lines[-1])

operator = None
operands = []
result = 0

def process_operation():
    global result
    global operands
    global operator

    print(operands)
    val = operands[0]
    for elt in operands[1:]:
        if operator == "*":
            val *= elt
        else:
            val += elt
    print(val)
    result += val

for c in range(C):
    if lines[-1][c] != " ":
        # New column
        # Process last accumulated values
        if c > 0:
            process_operation()

        # Set the new column
        operator = lines[-1][c]
        operands = []

    operand = 0
    seen = False
    for r in range(R):
        if lines[r][c] == " ":
            continue
        operand *= 10
        operand += int(lines[r][c])
        seen = True
    if seen:
        operands.append(operand)

# Process last column
process_operation()

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)