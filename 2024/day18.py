#!/usr/bin/env python

from aocd import puzzle, submit
from collections import defaultdict, deque

EXAMPLE_IDX = None
WIDTH = 70 + 1
ALWAYS_TIME = 1024 - 1

data = (puzzle.examples[EXAMPLE_IDX] if EXAMPLE_IDX is not None else puzzle).input_data

print(f"Puzzle #{puzzle.day}")

if EXAMPLE_IDX is not None:
    print(f"Using example #{EXAMPLE_IDX} data")
else:
    print(f"Using PROD data")

corrupted_times = {}

for time, line in enumerate(data.splitlines()):
    x, y = [int(x) for x in line.split(",")]
    if (x,y) not in corrupted_times:
        corrupted_times[(x, y)] = time

def is_corrupted(x, y, time, corrupted_time):
    time = ALWAYS_TIME # override
    corrupted_at = corrupted_time.get((x, y), 99999999999999999999999999)
    return time >= corrupted_at

def print_map(time, corrupted_times, path):
    for y in range(WIDTH):
        for x in range(WIDTH):
            if (x,y) in path:
                char = "O"
            elif is_corrupted(x, y, time, corrupted_times):
                char = "#"
            else:
                char = "."
            print(char, end="")
        print()

print(corrupted_times)
result = 0
q = deque()
q.append((0, 0, 0, set(), []))
while q:
    x, y, time, visited, path = q.popleft()
    #print(x, y, time)
    #print_map(time, corrupted_times, path)

    if x == WIDTH - 1 and y == WIDTH - 1:
        result = time
        break

    if x < 0 or y < 0 or x >= WIDTH or y >= WIDTH or (x, y) in visited:
        continue
    if is_corrupted(x, y, time, corrupted_times):
        continue

    visited.add((x, y))
    new_path = path + [(x,y)]

    q.append((x + 1, y, time + 1, visited, new_path))
    q.append((x - 1, y, time + 1, visited, new_path))
    q.append((x, y + 1, time + 1, visited, new_path))
    q.append((x, y - 1, time + 1, visited, new_path))

print(f"Result: {result}")
if EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)