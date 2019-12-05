"""
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

 -  112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
 -  123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
 -  111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle answer was 1102.


This solution is very similar to the previous solution but this time there's an additional check for the adjacent digits to have an exact count of 2.
"""
def check(password):
    if len(password) > 6:
        return False

    doubles = False
    for i, j in zip(password, password[1:]):
        if i > j:
            return False
        if i == j and password.count(i) == 2:
            doubles = True

    return doubles

input = "193651-649729".split('-')
count = 0
for i in range(int(input[0]), int(input[1])):
    if check(str(i)):
        count += 1

print(count)

    
