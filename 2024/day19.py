#!/usr/bin/env python

from aocd import puzzle, submit
from collections import defaultdict
import re
from tqdm import tqdm

EXAMPLE_IDX = 0

data = (puzzle.examples[EXAMPLE_IDX] if EXAMPLE_IDX is not None else puzzle).input_data

print(f"Puzzle #{puzzle.day}")

if EXAMPLE_IDX is not None:
    print(f"Using example #{EXAMPLE_IDX} data")
else:
    print(f"Using PROD data")

s1, s2 = data.split("\n\n")
available_towels = [s.strip() for s in s1.split(",")]

def is_possible_regex(line, towels):
    return re.match("^(" + "|".join(towels) + ")+$", line) != None

def is_possible_custom(line, towels, path):
    #print(f"{line=}")
    if not line:
        return path

    result = []
    for towel in towels:
        matches = line.startswith(towel)
        #print(f"{line=} {towel=} {matches=}")
        if matches:
            possible = is_possible_custom(line[len(towel):], towels, path + [towel])
            while possible and type(possible[0]) == list:
                possible = possible[0]
            if possible:
                result.append(possible)
    return result

def get_groupings(path, big_towels_possibilities_count):
    max_towel_length = max(len(x) for x in big_towels_possibilities_count.keys())

    explored_paths = {}
    print(f"{path=}")

    start = 0
    while start < len(path):
        print(f"{start=}")
        end = min(start + max_towel_length + 1, len(path))

        found_word = False
        while end > start:
            word = ""
            for sub_word in path[start:end]:
                word += sub_word
            print(f"{start=} {end=} {word=}")
            if word in big_towels_possibilities_count:
                found_word = True
                possibilities_count = big_towels_possibilities_count[word]
                print(f"{word} found in big towels -> adding {possibilities_count}")
                explored_path_possibilities_count += possibilities_count
                start += len(word)
                explored_path.append(word)
                break
            end -= 1
        
        if not found_word:
            explored_path.append(path[start])
            start += 1
        
        t = tuple(explored_path)
        if t in explored_paths:
            # We didn't explore a new path
            continue
        print(f"Adding new path {t=}")
        explored_path_possibilities_count = max(1, explored_path_possibilities_count) # It's 0 if the path cannot be grouped
        explored_paths[t] = explored_path_possibilities_count
    
    return explored_paths


BASE_TOWELS = ["w", "u", "b", "r", "g"]
base_towels_present = [towel for towel in BASE_TOWELS if towel in available_towels]

# Filter out all the useless towels as they can be constructed with the base ones
useful_towels = [towel for towel in available_towels if len(towel) == 1 or all(x for x in towel if x in base_towels_present)]

print(len(available_towels), "towels reduced to", len(useful_towels))
useful_towels_by_length = defaultdict(list)
max_towel_length = 0
for towel in useful_towels:
    useful_towels_by_length[len(towel)].append(towel)
    max_towel_length = max(len(towel), max_towel_length)

print(useful_towels)

big_towels_possibilities_count = {}
reduced_useful_towels = []
for i in range(max_towel_length + 1):
    for towel in useful_towels_by_length[i]:
        sub_towels = []
        for j in range(i - 1, 0, -1):
            sub_towels.extend(useful_towels_by_length[j])
        if is_possible_regex(towel, sub_towels):
            # Find the number of ways this towel can be constructed from our existing ones
            possibilities = is_possible_custom(towel, sub_towels, [])
            big_towels_possibilities_count[towel] = 0
            for possibility in possibilities:
                possibility_count = 0
                for word in possibility:
                    # This word can be constructed via sub towels
                    possibility_count += big_towels_possibilities_count.get(word, 0)
                big_towels_possibilities_count[towel] += possibility_count

            # This can be constructed with smaller towels
            continue

        # This can only be constructed with this one
        big_towels_possibilities_count[towel] = 1
        reduced_useful_towels.append(towel)

print(len(useful_towels), "towels reduced to", len(reduced_useful_towels))

reduced_useful_towels.sort(key=lambda x: len(x), reverse=True)
print(reduced_useful_towels)

print(big_towels_possibilities_count)

result = 0
for line in s2.splitlines():
    if is_possible_regex(line, reduced_useful_towels):
        print()
        print()
        print("evaluating", line)
        possibilities = is_possible_custom(line, reduced_useful_towels, [])
        possibilities_count = 0

        dedup_paths_with_count = {}
        for possibility in possibilities:
            paths_with_count = get_groupings(possibility, big_towels_possibilities_count)
            for path, count in paths_with_count.items():
                if path in dedup_paths_with_count:
                    assert count == dedup_paths_with_count[path]
                else:
                    dedup_paths_with_count[path] = count
                    possibilities_count += count
        print(f"{possibilities_count=}")
        result += possibilities_count

print(f"Result: {result}")
exit(0)
if EXAMPLE_IDX is None and data == puzzle.input_data:
    submit(result)