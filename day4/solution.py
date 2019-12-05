"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

 -  It is a six-digit number.
 -  The value is within the range given in your puzzle input.
 -  Two adjacent digits are the same (like 22 in 122345).
 -  Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

 -  111111 meets these criteria (double 11, never decreases).
 -  223450 does not meet these criteria (decreasing pair of digits 50).
 -  123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

    Your puzzle answer was 1605.


Pretty self explanatory.
Loop through all inputs check the value and see if its valid.

Check if password has
 - a length greater than 6
 - a double
 - non-decreasing value
"""
def check(password):
    if len(password) > 6:
        return False

    doubles = False
    for i, j in zip(password, password[1:]):
        if i > j:
            return False
        if i == j:
            doubles = True

    return doubles

input = "193651-649729".split('-')
count = 0
for i in range(int(input[0]), int(input[1])):
    if check(str(i)):
        count += 1

print(count)

    
