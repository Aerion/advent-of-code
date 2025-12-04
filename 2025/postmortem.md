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