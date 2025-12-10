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

def get_min_count(target_indicators: int, buttons: list[int]):
    q = deque()
    q.append((0, []))

    while q:
        indicators, initial_path = q.popleft()

        for button in buttons:
            path = initial_path + [button]

            """
            for btn_path in path:
                print(f"{btn_path:b}", end=", ")
            print()
            print(f'{indicators=:b} {button=:b}')
            """

            indicators ^= button
            if indicators == target_indicators:
                for btn_path in path:
                    print(f"{btn_path:b}", end=", ")
                print()
                print(path)
                return len(path)
            q.append((indicators, path))

            indicators ^= button


def parse_indicators(indicators_str: str):
    indicators = 0
    for c in indicators_str:
        indicators <<= 1
        indicators |= c == "#"
    return indicators

def parse_buttons(buttons_str: list[str], indicators_len: int):
    buttons = []

    for button_str in buttons_str:
        button = 0
        for elt in button_str[1:-1].split(","):
            button |= 1 << (indicators_len - int(elt) - 1)
        buttons.append(button)

    return buttons

result = 0
for line in data.splitlines():
    elts = line.split(" ")
    indicators_list = [x == '#' for x in elts[0][1:-1]]
    indicators = parse_indicators(elts[0][1:-1])
    buttons_list = [[int(i) for i in x[1:-1].split(",")] for x in elts[1:-1]]
    buttons = parse_buttons(elts[1:-1], len(indicators_list))

    print(f"{indicators=:b}")
    #print(f"{indicators_list=}")
    for button in buttons:
        print(f"{button=:b}", end=", ")
    print()
    #print(f"{buttons_list=}")

    min_count = get_min_count(indicators, buttons)
    print(min_count)
    result += min_count

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)