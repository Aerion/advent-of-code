#!/usr/bin/env python

from aocd import puzzle, submit
from collections import defaultdict
from functools import cache

EXAMPLE_IDX = 0

data = (puzzle.examples[EXAMPLE_IDX] if EXAMPLE_IDX is not None else puzzle).input_data
if EXAMPLE_IDX == 0:
    data = """029A
980A
179A
456A
379A"""

print(f"Puzzle #{puzzle.day}")

if EXAMPLE_IDX is not None:
    print(f"Using example #{EXAMPLE_IDX} data")
else:
    print(f"Using PROD data")

numpad = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3),
}

dirpad = {
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

vector_by_numpad_dir = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

@cache
def get_final_dirpad_sequences(start, target):
    pass

@cache
def get_numpad_sequences_for_button(start, target):
    return numpad_dfs(numpad[start], numpad[target], [])

def debug(str):
    return
    print(str)

def numpad_dfs(start_pos: tuple[int, int], end_pos: tuple[int, int], path: list[str]):
    if start_pos == end_pos:
        # Won
        return [path + ["A"]]

    possibilities = []
    if start_pos[0] < end_pos[0]:
        possibilities.append('>')
    if start_pos[0] > end_pos[0]:
        possibilities.append('<')
    if start_pos[1] < end_pos[1]:
        possibilities.append('v')
    if start_pos[1] > end_pos[1]:
        possibilities.append('^')

    debug(possibilities)
    
    result = []
    for possibility in possibilities:
        x_inc, y_inc = vector_by_numpad_dir[possibility]
        new_x, new_y = start_pos[0] + x_inc, start_pos[1] + y_inc
        if (new_x, new_y) == (0, 3):
            debug("Inaccessible empty gap")
            continue
        if new_x < 0 or new_x > 2 or new_y < 0 or new_y > 3:
            assert False # If we end up there, the possibilities were badly computed

        path.append(possibility)
        for valid_path in numpad_dfs((new_x, new_y), end_pos, path):
            result.append(tuple(valid_path))
        path.pop()
    
    return result

def get_numpad_sequences_for_full_line(idx, input, output):
    if idx == len(input):
        return [output]

    numpad_target = line[idx]
    start = 'A' if idx == 0 else line[idx - 1]
    
    numpad_sequences = get_numpad_sequences_for_button(start, numpad_target)

    result = []
    for sequence in numpad_sequences:
        for leaf_output in get_numpad_sequences_for_full_line(idx + 1, input, output + sequence):
            result.append(tuple(leaf_output))
    
    return result


result = 0
for line in data.splitlines():
    code = int(line[:-1])
    line_result = 0

    numpad_sequences = ["".join(x) for x in get_numpad_sequences_for_full_line(0, line, ())]
    print(numpad_sequences)
    continue
    result += line_result * code
    exit(0)

print(f"Result: {result}")
if EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)