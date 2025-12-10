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
from z3 import *

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
for line in data.splitlines():
    elts = line.split(" ")
    buttons_list = [[int(i) for i in x[1:-1].split(",")] for x in elts[1:-1]]
    joltages_list = [int(x) for x in elts[-1][1:-1].split(",")]

    opt = Optimize()

    button_vars = []
    for i, button in enumerate(buttons_list):
        var = Int(f'btn_{i}')
        button_vars.append(var)
        opt.add(var >= 0)
    
    for joltage_i, joltage in enumerate(joltages_list):
        expr = 0
        for btn_i, button in enumerate(buttons_list):
            if joltage_i in button:
                # This button affects the joltage target
                expr += button_vars[btn_i]
        
        opt.add(joltage == expr)

    print(f"{buttons_list=}")
    print(f"{joltages_list=}")
    opt.minimize(Sum(button_vars))
    
    print(opt)
    assert opt.check() == sat
    model = opt.model()

    presses = [model[btn_var].as_long() for btn_var in button_vars]
    min_count = sum(presses)

    result += min_count

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)