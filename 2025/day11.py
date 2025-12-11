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
class Node:
    name: str
    children: list[Node]

parents_by_node_name: dict[str, list[Node]] = defaultdict(list)

dot_output = ""

nodes_by_name: dict[str, Node] = {}
for line in data.splitlines():
    root_name, elts_str = line.split(':')
    elts_names = elts_str.split(' ')

    for name in (root_name, *elts_names):
        if name not in nodes_by_name:
            nodes_by_name[name] = Node(name, [])

    for neighbor_name in elts_names:
        nodes_by_name[root_name].children.append(nodes_by_name[neighbor_name])
        parents_by_node_name[neighbor_name].append(nodes_by_name[root_name])

    dot_output += f'{root_name} -> {{{" ".join(elts_names)} }}\n'

with open('/tmp/out.dot', 'w+') as out_f:
    out_f.write(dot_output)


result = 0
q: deque[Node] = deque()
q.append(nodes_by_name['you'])
while q:
    node = q.popleft()
    if node.name == 'out':
        result += 1
        continue

    for child in node.children:
        q.append(child)

#################################################################
# No changes after this line
#################################################################

_end_time = time.time()
print(f"Result: {result} (in {timedelta(seconds=_end_time - _start_time)})", file=stderr)
if result is not None and EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)