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