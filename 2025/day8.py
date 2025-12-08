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

@dataclass
class CircuitId:
    id_: int

    def __eq__(self, value):
        return self.id_ == value.id_

@dataclass(unsafe_hash=True)
class Box:
    x: int
    y: int
    z: int
    connected_to: list[Box] = field(hash=False)
    circuit_id: Optional[CircuitId] = field(hash=False)

    def distance_from(self, other: Box):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

boxes: list[Box] = []
for i, line in enumerate(data.splitlines()):
    x, y, z = line.split(",")
    box = Box(int(x), int(y), int(z), [], None)
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

circuit_id_count = 0
existing_circuit_ids = set()

def set_circuit_id(root: Box, id: CircuitId):
    def set_circuit_id_rec(box: Box):
        if box in seen:
            return

        seen.add(box)
        box.circuit_id = id

        for neighbor in box.connected_to:
            set_circuit_id_rec(neighbor)

    seen = set()
    set_circuit_id_rec(box)

indexes.sort(key=lambda elt: distances[elt[0]][elt[1]])
count = 0
for i, j in indexes:
    count += 1
    box = boxes[i]
    other_box = boxes[j]
    box.connected_to.append(other_box)
    other_box.connected_to.append(box)

    #print(count)

    # One of them has an id
    if box.circuit_id is None and other_box.circuit_id is not None:
        set_circuit_id(box, other_box.circuit_id)
    elif box.circuit_id is not None and other_box.circuit_id is None:
        set_circuit_id(other_box, box.circuit_id)
    elif box.circuit_id is None and other_box.circuit_id is None:
        circuit_id_count += 1
        box.circuit_id = CircuitId(circuit_id_count)
        set_circuit_id(other_box, box.circuit_id)
        existing_circuit_ids.add(circuit_id_count)
    elif box.circuit_id != other_box.circuit_id:
        # Two other circuits, unify them
        #print(existing_circuit_ids)
        #print(box.circuit_id, other_box.circuit_id)
        existing_circuit_ids.remove(other_box.circuit_id.id_)
        set_circuit_id(other_box, box.circuit_id)

    circuits_count = set((x.circuit_id.id_ for x in boxes if x.circuit_id))
    if len(circuits_count) == 1 and all((len(x.connected_to) > 0 for x in boxes)):
        print("Latest one")
        print(count, len(indexes))
        result = box.x * other_box.x
        break
    """
    for b in boxes:
        for c in b.connected_to:
            if not b.circuit_id == c.circuit_id:
                print(b, c)
            assert b.circuit_id == c.circuit_id
        if b.circuit_id is not None and b.circuit_id.id_ not in existing_circuit_ids:
            for bi in boxes:
                print(bi)
            assert False
    """

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)