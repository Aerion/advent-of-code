#!/usr/bin/env python

from aocd import puzzle, submit
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import timedelta
from functools import cache
from rich import print
from sys import stderr
from typing import Optional
import math
import time
from tqdm import tqdm

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

@dataclass(unsafe_hash=True)
class Box:
    x: int
    y: int
    z: int
    connected_to: list[Box] = field(hash=False)

    def distance_from(self, other: Box):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

boxes: list[Box] = []
for line in data.splitlines():
    x, y, z = line.split(",")
    box = Box(int(x), int(y), int(z), [])
    boxes.append(box)

distances = [[None] * len(boxes) for _ in range(len(boxes))]
indexes = []
for i, box in enumerate(boxes):
    for j, other_box in enumerate(boxes):
        if i == j or distances[i][j]:
            continue

        distance = box.distance_from(other_box)
        distances[i][j] = distance
        distances[j][i] = distance
        indexes.append((i, j))

JUNCTIONS_COUNT = 1000
indexes.sort(key=lambda elt: distances[elt[0]][elt[1]])
for i, j in indexes[:JUNCTIONS_COUNT]:
    box = boxes[i]
    other_box = boxes[j]
    box.connected_to.append(other_box)
    other_box.connected_to.append(box)
    #print(box, other_box, "connected")

def explore_circuit(box: Box, seen: set[Box], circuit: list[Box]):
    if box in seen:
        return

    seen.add(box)
    circuit.append(circuit)

    for neighbor in box.connected_to:
        explore_circuit(neighbor, seen, circuit)

circuits: list[list[Box]] = []
seen = set()
for box in boxes:
    circuit: list[Box] = []
    explore_circuit(box, seen, circuit)
    circuits.append(circuit)

circuits.sort(key=lambda c: len(c), reverse=True)
result = 1
for circuit in circuits[:3]:
    result *= len(circuit)

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)