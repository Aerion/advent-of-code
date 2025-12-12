# Day 1

## Part 1

- Sign error for `R` / `L` direction, wasn't impacting the result but it didn't follow the statement

## Part 2

- Negative modulo in Python behaves differently than other languages (`-5 % 100 = 95` \[python] instead of `-5 % 100 = -5` \[js])
- To bypass this, I wrongly did `(val+99) % 100` instead of `(val+100) % 100`
- Didn't read the last lines of the exercise indicating that a single rotation could be larger than `100`
- Tried to go too fast to have a result as it was day1 and should be easy, waited too much before trying with simple examples

## Conclusions

- Read the problem statement in its entirety
- Use simple examples to debug issues
- Know that [python modulo behaves](https://stackoverflow.com/questions/3883004/how-does-the-modulo-operator-work-on-negative-numbers-in-python) in a different way than other languages

# Day 2

## Part 1

N/A

## Part 2

- Lost too much time trying to get the boundaries of the split
- Didn't take into account the single digits number, which impacted the end result

## Conclusions

- It's better to spend 1 min thinking properly about array indexes than to spend 5 mins down the line trying to make working wrong ones defined in 2s
- Think about extreme edge cases: here I was doing tunnel vision and missed the single digits that were the cause for the bad result

# Day 3

## Part 1

- Initial implementation was flawed because it considered it as just taking the 2 max values of the array

## Part 2

- The range high range conditions could be improved in legibility rather than being the result of 4 operands `len(bank) - REQUIRED_BATTERY_COUNT + battery_idx + 1`

## Conclusions

- Read the examples a second time to make sure to understand what's being asked
- Add a comment or use intermediate variables for conditions that end up being complex due to variables count

# Day 4

## Part 1

N/A

## Part 2

- Spent a bit of time trying to think about a better solution than the one being displayed in the problem statement, but wasn't needed
- Code is messy (grid, new_grid, duplication of lots of code, is_valid with different types)

## Conclusions

N/A

# Day 5

## Part 1

- Having separate methods simplify readability

## Part 2

- Didn't think about all the edge cases right away

## Conclusions

N/A

# Day 6

## Part 1

N/A

## Part 2

- Overlooked the fact that the space padding was important, which wasted time on trying to fit one right aligned example, then understanding a left aligned one
- Spent too much time trying to work on the part1 algorithm
- Was way simpler to start over as it's natural to process column by column and handling the padding for part2

## Conclusions

- Make sure to understand the edge cases that are presented in the example
- Take a step back if stuck, clearing the existing implementation isn't a bad thing
- Visualize the input data by running `aocd` and `less -RS` or `bat -S`

# Day 7

## Part 1

- I made sure to understand exactly where the example result comes from
- Using `assert` is nice to confirm assumptions about the problem

## Part 2

N/A

## Conclusions

N/A

# Day 8

## Part 1

- Using adjacency matrix could be better (but tbd for readability)
- Lost time with hashes of the dataclass

## Part 2

- Failed unifying the circuits in a "beautiful" manner and resorted to doing a DFS on all the connected ones. Though having the circuitid as a reference could have simplified this
- Code is not clean
- Exercise wasn't difficult in itself, I spent most of the time trying to make the circuitid working
- It seems I tried to implement the idea of Union Find, without knowing it

## Conclusions

- Check out Union Find

# Day 9

## Part 1

- For consistency make sure to adapt `r` and `c` to match the `x`, `y` coordinates of the example

## Part 2

- Good thing to test approaches on both the example and the input to fail early if it's too long (e.g. dfs/bfs outside or inside bounds)
- Tried many approaches that in the end were too long because of iteration over many points
- I know storing the points is unoptimized, and the result takes 5 min to execute, but I didn't find a better solution
- Will need to think again about it or to check out other solutions

## Conclusions

- Check out the solutions for this exercise afterwards

# Day 10

## Part 1

- Fun to use bitmasks but would have worked just fine in initial implem with lists

## Part 2

- Tried solutions with BFS but couldn't work with input
- Use `deque.popleft()` instead of `deque.pop()` to do a BFS
- Unfortunately have to resort to z3 solver, which required to see how to do it
- Spent a bit of time trying to wrap my head around how to materialize this in a proper equation with z3

## Conclusions

- Keep `popleft` in mind for `deque``
- Don't be afraid to use `z3` for aoc even if it may be disappointing

# Day 11

## Part 1

N/A

## Part 2

N/A

## Conclusions

N/A

# Day 12

## Part 1

- Checking the input requirements showcases the feasibility

## Conclusions

- Assume that AoC last puzzle is easy to solve, and to check the input for quick win :)